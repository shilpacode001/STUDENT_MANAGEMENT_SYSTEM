from django.db import models


class StudentMark(models.Model):
    s_name=models.CharField(max_length=30,verbose_name='Student Name')
    phy=models.IntegerField(verbose_name='Physics')
    chem=models.IntegerField(verbose_name='Chemistry')
    math=models.IntegerField(verbose_name='Maths')
    
    def __str__(self):
        return self.s_name

class UploadFiles(models.Model):
    file_name=models.CharField(max_length=50,verbose_name="File name")
    file_upload=models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.file_name