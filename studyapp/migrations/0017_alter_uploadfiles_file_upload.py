# Generated by Django 5.0.6 on 2024-07-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0016_alter_uploadfiles_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file_upload',
            field=models.FileField(upload_to='media/'),
        ),
    ]
