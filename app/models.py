from django.db import models

# Create your models here.
"""
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.

新增字段时会提示：
1 让你自己输入一个值作为新增字段的默认值
2 退出 创建字段时自己加 default=‘’
"""


class Department(models.Model):
    """ 部门 """
    title = models.CharField(verbose_name='标题', max_length=32)


class UserInfo(models.Model):
    """ 员工 """
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')

    # 账户余额十位数 两位小数 默认值为 0
    account = models.DecimalField(
        verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(
        verbose_name='入职时间', null=True, blank=True)

    # 连表
    # depart 字段在 Django 中会自动加上 _id 生成为 depart_id
    # to 要关联的表名称    to_fields 要关联的表的字段名
    # on_delete=models.CASCADE()  级联删除 如果部门删除那么关联员工数据也删除
    # depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)

    # on_delete=models.SET_NULL() 置空 如果部门删除那么关联员工数据部门字段置空
    depart = models.ForeignKey(
        to='Department', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)

    # SmallIntegerField 小整形
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(
        verbose_name='性别', choices=gender_choices, default='1')
