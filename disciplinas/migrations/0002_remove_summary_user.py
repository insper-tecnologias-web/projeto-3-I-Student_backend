# Generated by Django 4.0.4 on 2022-06-05 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='user',
        ),
    ]
