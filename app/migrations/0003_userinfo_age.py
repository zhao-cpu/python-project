# Generated by Django 4.2.1 on 2023-05-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userinfo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
            preserve_default=False,
        ),
    ]
