# Generated by Django 4.0.4 on 2022-05-31 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_course_name', models.CharField(max_length=50, unique=True)),
                ('display_course_name', models.CharField(max_length=50, unique=True)),
                ('number_of_semesters', models.IntegerField()),
                ('description', models.TextField()),
                ('background_img', models.ImageField(upload_to='images/')),
                ('img_description', models.CharField(default=models.CharField(max_length=50, unique=True), max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_subject_name', models.CharField(max_length=50, unique=True)),
                ('display_subject_name', models.CharField(max_length=50, unique=True)),
                ('semester', models.IntegerField()),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplinas.course')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='resumos/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplinas.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
