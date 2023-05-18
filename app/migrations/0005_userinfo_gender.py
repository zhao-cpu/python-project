# Generated by Django 4.2.1 on 2023-05-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_userinfo_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default='1', verbose_name='性别'),
        ),
    ]