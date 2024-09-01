# Generated by Django 5.0.6 on 2024-06-29 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studyapp', '0009_delete_student_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('max_marks', models.IntegerField()),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyapp.student')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyapp.subject')),
            ],
        ),
    ]
