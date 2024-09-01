from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('delete/<str:s_name>/',views.delete,name='delete'),
    path('update/<str:s_name>/',views.update,name='update'),
    path('deletenote/<str:file_name>',views.deletenote,name='deletenote'),
    path('create',views.create,name='create'),
    path('upload',views.upload,name='upload'),
    path('faculty',views.faculty,name='faculty'),
    path('view',views.view,name='view'),
    path('signup',views.signup,name='signup')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)