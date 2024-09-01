from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import StudentMark,UploadFiles
from .forms import UploadForm

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def login_view(request):
    if request.method=='POST':
        usern=request.POST['uname']
        pswd=request.POST['pwd']
        user=authenticate(request,username=usern,password=pswd)
        if user is not None:
            res={'nme':usern}
            if user.groups.filter(name='student').exists():
                login(request,user)
                try:
                    st_one=StudentMark.objects.get(s_name=usern)
                    res['stud']=st_one
                    return render(request,"result.html",res)
                except: 
                    res['msg']="No scores to display. You have not attended any exams yet."
                    return render(request,"result.html",res)
            elif user.groups.filter(name='faculty').exists():
                login(request,user)
                st_all=StudentMark.objects.all()
                res['allstud']=st_all
                return render(request,"facultypage.html",res)
            else:
                res['err']='Invalid username or password'
                return render(request, "login.html", res)
                
    else:        
        return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def delete(request,s_name):
    res={}
    delst=StudentMark.objects.get(s_name=s_name)
    delst.delete()
    return redirect("faculty")

def deletenote(request,file_name):
    deln=UploadFiles.objects.get(file_name=file_name)
    deln.delete()
    return redirect('view')    

def update(request,s_name):
    res={}
    if request.method=="POST":
        a_st=StudentMark.objects.get(s_name=s_name)
        a_st.phy=request.POST['t1']
        a_st.chem=request.POST['t2']
        a_st.math=request.POST['t3']
        a_st.save()
        return redirect('faculty') 
    else:       
        return render(request,"edit.html",{'msg':s_name})
def create(request):
    res={}
    if request.method=="POST":
        st_name=request.POST['st_name']
        st_ph=request.POST['ph']
        st_ch=request.POST['ch']
        st_ma=request.POST['ma']
        st_new=StudentMark(s_name=st_name,phy=st_ph,chem=st_ch,math=st_ma)
        st_new.save()
        return redirect("faculty")
    else:
        return render(request,"addmark.html")
def upload(request):
    res={}
    if request.method=="POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            res['msg1']='Uploaded successfully'
        else:
            res['msg1']='Form is not valid'   

    form1=UploadForm()
    res['form']=form1
    return render(request,"fileupload.html",res)

def faculty(request):
    res={}
    st_all=StudentMark.objects.all()

    """group_name='student'
    group=Group.objects.get(name=group_name)
    all_list=group.user_set.all()
    res['alllist']=all_list """

    res['allstud']=st_all
    return render(request,"facultypage.html",res)

def view(request):
    res={}
    note=UploadFiles.objects.all()
    res['notes']=note
    if request.method=='POST':
        return render(request,"downnotes.html",res)
    else:
        return render(request,"viewnotes.html",res)

def signup(request):
    if request.method=='POST':
        uname=request.POST['usern1']
        pwd=request.POST['pwd1']
        user1=User.objects.create_user(username=uname,password=pwd)
        user1.save()
        group_name='student'
        group=Group.objects.get(name=group_name)
        user1.groups.add(group)
        return render(request,"signup.html",{'msg1':"New Student signup successful"})
            

    return render(request,"signup.html")