# Generated by Django 5.0.6 on 2024-07-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0017_alter_uploadfiles_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file_name',
            field=models.CharField(max_length=50, verbose_name='File name'),
        ),
        migrations.AlterField(
            model_name='uploadfiles',
            name='file_upload',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
