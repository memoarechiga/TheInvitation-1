# Generated by Django 4.1.7 on 2023-03-29 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]