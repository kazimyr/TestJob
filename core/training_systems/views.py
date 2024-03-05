# from datetime import datetime
from django.shortcuts import render
from django.http import QueryDict
from training_systems.models import Product, Lesson, Group

def course(request):
    qs_products = Product.objects.all()
    for each in qs_products:
        each.lessons = Lesson.objects.filter(product = each).count()
        group = Group.objects.filter(product = each)
        each.users_quantity = 0
        for gr in group:
            each.users_quantity += gr.users_quantity
    context = {
        'title' : 'Курсы',
        'courses' : qs_products,
    }
    return render(request, 'index.html', context)

    
def lessons(request):
    course_name = request.GET.__getitem__('l')
    # get = request.GET.copy()
    # course_name = get.pop('l')
    id_product = Product.objects.get(name = course_name).id
    qs_lessons = Lesson.objects.filter(product = id_product).order_by('pk')
    for i in range(0, len(qs_lessons)):
        qs_lessons[i].number = i + 1
    context = {
        'title': 'Уроки',
        'course_name': course_name,
        'lessons': qs_lessons,
        # [
        #     {'name':'Урок1', 'video': ''},
        #     {'name':'Урок2', 'video': ''},
        #     {'name':'Урок3', 'video': ''},
        # ]
    }
    return render(request,'lessons.html', context)


def group(request):
    if request.GET.get('re', default = ''):
        Group.resort_users()

    courses = request.GET.getlist('cr')
    for each in courses:
        Group.add_user(Product.objects.get(name = each).pk)
    gr = Group.objects.all().order_by('name')
    context = {
        'title': 'Группы',
        'groups' : gr,
    }
    return render(request,'group.html', context)