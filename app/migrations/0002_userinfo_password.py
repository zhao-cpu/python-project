# Generated by Django 4.2.1 on 2023-05-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default='', max_length=64, verbose_name='密码'),
            preserve_default=False,
        ),
    ]
