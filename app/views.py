from django import forms
from django.shortcuts import render, HttpResponse, redirect

from app import models


def depart_list(request):
    depart_list = models.Department.objects.all()
    return render(request, 'depart_list.html', {"depart_list": depart_list})


def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect('/depart/list')


def depart_delete(request, id):
    models.Department.objects.filter(id='3').delete()
    return HttpResponse('delete')


def user_list(request):
    user_list = models.UserInfo.objects.all()
    # for user in user_list:
    # print(
    #     user.depart_id, user.depart.title,
    #     user.create_time, user.create_time.strftime("%Y-%m-%d %H:%M:%S"),
    #     user.gender, user.get_gender_display()
    # )
    return render(request, 'user_list.html', {"user_list": user_list})


class UserModelForm(forms.ModelForm):

    # 添加验证
    name = forms.CharField(min_length=2, label="用户")

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account',
                  'create_time', 'depart', 'gender']

        # 如果表单很多会很麻烦，优化
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control custom", "placeholder": "请输入名称"}),
        #     "password": forms.PasswordInput()
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # name <django.forms.fields.CharField object at 0x0000029D17DB0450>
            # password <django.forms.fields.CharField object at 0x0000029D17DB0690>
            # ...
            # print(name, field)

            if name == 'password':
                pass

            field.widget.attrs = {
                "class": "form-control", "placeholder": field.label}


def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {"form": form})

    form = UserModelForm(data=request.POST)
    # 验证是否为空
    if form.is_valid():
        print(form.cleaned_data)
        # 保存
        form.save()
        return redirect('/user/list')

    print(form.errors)
    return render(request, 'user_add.html', {"form": form})
