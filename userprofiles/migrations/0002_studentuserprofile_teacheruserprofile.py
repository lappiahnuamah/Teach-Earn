# Generated by Django 3.2.6 on 2021-09-22 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.CharField(max_length=100)),
                ('teachers_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='StudentUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('student_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.userprofile')),
            ],
        ),
    ]
