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
