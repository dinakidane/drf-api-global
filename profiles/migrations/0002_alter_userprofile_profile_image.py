# Generated by Django 5.1.1 on 2024-09-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='../samples/default_profile_ky9c7z', upload_to='images/'),
        ),
    ]
