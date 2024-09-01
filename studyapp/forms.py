from django import forms
from .models import UploadFiles

class UploadForm(forms.ModelForm):
    class Meta:
        model=UploadFiles
        fields=['file_name','file_upload']