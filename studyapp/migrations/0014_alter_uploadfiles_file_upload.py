# Generated by Django 5.0.6 on 2024-07-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0013_alter_uploadfiles_file_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file_upload',
            field=models.FileField(upload_to='notes'),
        ),
    ]
