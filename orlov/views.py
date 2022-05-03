from django.shortcuts import render, redirect

# Класс HttpResponse из пакета django.http, который позволяет отправить текстовое содержимое.
from django.http import HttpResponse
# Конструктор принимает один обязательный аргумент – путь для перенаправления. Это может быть полный URL (например, 'https://www.yahoo.com/search/') или абсолютный путь без домена (например, '/search/').
from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Подключение моделей
from .models import Position, Employee, Application, Movement, Person, News
# Подключение форм
from .forms import PositionForm, EmployeeForm, ApplicationForm, MovementForm, PersonForm, NewsForm, SignUpForm
#from .forms import SignUpForm

import datetime

#import xlwt

from django.db import models

import sys

#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy

from django.contrib.auth import login as auth_login

# Групповые ограничения
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='403')

# Стартовая страница
# Стартовая страница
#@login_required 
def index(request):
    return render(request, "index.html")

# Страница Контакты
def contact(request):
    return render(request, "contact.html")

# Страница Отчеты
def report(request):
    view_orders = View_Orders.objects.all().order_by('dateo')
    return render(request, "report.html", {"view_orders": view_orders})

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def position_index(request):
    position = Position.objects.all().order_by('title')
    return render(request, "position/index.html", {"position": position})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def position_create(request):
    if request.method == "POST":
        position = Position()        
        position.title = request.POST.get("title")
        position.save()
        return HttpResponseRedirect(reverse('position_index'))
    else:        
        positionform = PositionForm()
        return render(request, "position/create.html", {"form": positionform})

# Функция edit выполняет редактирование объекта.
@login_required
@group_required("Managers")
def position_edit(request, id):
    try:
        position = Position.objects.get(id=id) 
        if request.method == "POST":
            position.title = request.POST.get("title")
            position.save()
            return HttpResponseRedirect(reverse('position_index'))
        else:
            # Загрузка начальных данных
            positionform = PositionForm(initial={'title': position.title, })
            return render(request, "position/edit.html", {"form": positionform})
    except Position.DoesNotExist:
        return HttpResponseNotFound("<h2>Position not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def position_delete(request, id):
    try:
        position = Position.objects.get(id=id)
        position.delete()
        return HttpResponseRedirect(reverse('position_index'))
    except Position.DoesNotExist:
        return HttpResponseNotFound("<h2>Position not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def position_read(request, id):
    try:
        position = Position.objects.get(id=id) 
        return render(request, "position/read.html", {"position": position})
    except Position.DoesNotExist:
        return HttpResponseNotFound("<h2>Position not found</h2>")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def employee_index(request):
    employee = Employee.objects.all().order_by('surname')
    return render(request, "employee/index.html", {"employee": employee})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def employee_create(request):
    if request.method == "POST":
        employee = Employee()
        employee.surname = request.POST.get("surname")
        employee.name = request.POST.get("name")
        employee.patronymic = request.POST.get("patronymic")
        employee.sex = request.POST.get("sex")
        employee.birthday = request.POST.get("birthday")
        employee.address = request.POST.get("address")
        employee.phone = request.POST.get("phone")
        employee.position = Position.objects.filter(id=request.POST.get("position")).first()
        employee.save()
        return HttpResponseRedirect(reverse('employee_index'))
    else:        
        employeeform = EmployeeForm()
        return render(request, "employee/create.html", {"form": employeeform})

# Функция edit выполняет редактирование объекта.
@login_required
@group_required("Managers")
def employee_edit(request, id):
    try:
        employee = Employee.objects.get(id=id) 
        if request.method == "POST":
            employee.surname = request.POST.get("surname")
            employee.name = request.POST.get("name")
            employee.patronymic = request.POST.get("patronymic")
            employee.sex = request.POST.get("sex")
            employee.birthday = request.POST.get("birthday")
            employee.address = request.POST.get("address")
            employee.phone = request.POST.get("phone")
            employee.position = Position.objects.filter(id=request.POST.get("position")).first()        
            employee.save()
            return HttpResponseRedirect(reverse('employee_index'))
        else:
            # Загрузка начальных данных
            employeeform = EmployeeForm(initial={'surname': employee.surname, 'name': employee.name, 'patronymic': employee.patronymic, 'sex': employee.sex, 'birthday': employee.birthday.strftime('%Y-%m-%d'), 'address': employee.address, 'phone': employee.phone, 'position': employee.position, })
            return render(request, "employee/edit.html", {"form": employeeform})
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Employee not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def employee_delete(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return HttpResponseRedirect(reverse('employee_index'))
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Employee not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def employee_read(request, id):
    try:
        employee = Employee.objects.get(id=id) 
        return render(request, "employee/read.html", {"employee": employee})
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Employee not found</h2>")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def application_index(request):
    application = Application.objects.all().order_by('datea')
    return render(request, "application/index.html", {"application": application})

# Список 
@login_required
def application_list(request):
    #application = Application.objects.all().order_by('datea')
    print(request.user.id)
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    application = Application.objects.filter(user_id=request.user.id).order_by('-datea')
    return render(request, "application/list.html", {"application": application, 'first_name': first_name, 'last_name': last_name, 'email': email})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
#@group_required("Managers")
def application_create(request):
    if request.method == "POST":
        application = Application()
        application.title = request.POST.get("title")
        application.details = request.POST.get("details")
        application.user_id = request.user.id
        application.save()
        return HttpResponseRedirect(reverse('application_list'))
    else:        
        applicationform = ApplicationForm()
        return render(request, "application/create.html", {"form": applicationform})

# Функция edit выполняет редактирование объекта.
@login_required
@group_required("Managers")
def application_edit(request, id):
    try:
        application = Application.objects.get(id=id) 
        if request.method == "POST":
            application.title = request.POST.get("title")
            application.details = request.POST.get("details")
            application.save()
            return HttpResponseRedirect(reverse('application_index'))
        else:
            # Загрузка начальных данных
            applicationform = ApplicationForm(initial={'title': application.title, 'details': application.details, })
            return render(request, "application/edit.html", {"form": applicationform})
    except Application.DoesNotExist:
        return HttpResponseNotFound("<h2>Application not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def application_delete(request, id):
    try:
        application = Application.objects.get(id=id)
        application.delete()
        return HttpResponseRedirect(reverse('application_index'))
    except Application.DoesNotExist:
        return HttpResponseNotFound("<h2>Application not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def application_read(request, id):
    try:
        application = Application.objects.get(id=id)
        movement = Movement.objects.filter(application_id=id).order_by('-datem')
        return render(request, "application/read.html", {"application": application, "movement": movement})
    except Application.DoesNotExist:
        return HttpResponseNotFound("<h2>Application not found</h2>")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def movement_index(request, application_id):
    movement = Movement.objects.filter(application_id=application_id).order_by('-datem')
    app = Application.objects.get(id=application_id)
    #movement = Movement.objects.all().order_by('-orders', '-datem')
    return render(request, "movement/index.html", {"movement": movement, "application_id": application_id, "app": app})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def movement_create(request, application_id):
    app = Application.objects.get(id=application_id)
    if request.method == "POST":
        movement = Movement()
        movement.application_id = application_id
        movement.datem = datetime.datetime.now()
        movement.status = request.POST.get("status")
        movement.details = request.POST.get("details")
        movement.employee = Employee.objects.filter(id=request.POST.get("employee")).first()
        movement.save()
        return HttpResponseRedirect(reverse('movement_index', args=(application_id,)))
    else:
        movementform = MovementForm(initial={ 'datem': datetime.datetime.now().strftime('%Y-%m-%d')})
        return render(request, "movement/create.html", {"form": movementform, "application_id": application_id, "app": app})

# Функция edit выполняет редактирование объекта.
@login_required
@group_required("Managers")
def movement_edit(request, id, application_id):
    app = Application.objects.get(id=application_id)
    try:
        movement = Movement.objects.get(id=id) 
        if request.method == "POST":
            movement.datem = datetime.datetime.now()
            movement.status = request.POST.get("status")
            movement.details = request.POST.get("details")
            movement.employee = Employee.objects.filter(id=request.POST.get("employee")).first()
            movement.save()
            print(application_id)
            return HttpResponseRedirect(reverse('movement_index', args=(application_id,)))
        else:
            # Загрузка начальных данных
            movementform = MovementForm(initial={'application': movement.application, 'datem': movement.datem.strftime('%Y-%m-%d'), 'status': movement.status, 'details': movement.details,  'employee': movement.employee, })
            return render(request, "movement/edit.html", {"form": movementform, "application_id": application_id, "app": app})
    except Movement.DoesNotExist:
        return HttpResponseNotFound("<h2>Movement not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def movement_delete(request, id, application_id):
    try:
        movement = Movement.objects.get(id=id)
        movement.delete()
        return HttpResponseRedirect(reverse('movement_index', args=(application_id,)))
    except Movement.DoesNotExist:
        return HttpResponseNotFound("<h2>Movement not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def movement_read(request, id, application_id):
    try:
        movement = Movement.objects.get(id=id) 
        return render(request, "movement/read.html", {"movement": movement, "application_id": application_id})
    except Movement.DoesNotExist:
        return HttpResponseNotFound("<h2>Movement not found</h2>")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def person_index(request):
    person = Person.objects.all().order_by('user')
    return render(request, "person/index.html", {"person": person})

# Функция edit выполняет редактирование объекта.
@login_required
#def person_edit(request, id):
def person_edit(request):
    try:
        #person = Person.objects.get(id=id)
        print(request.user.id)
        person = Person.objects.get(user_id=request.user.id)        
        if request.method == "POST":
            person.phone = request.POST.get("phone")
            person.address = request.POST.get("address")
            person.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            # Загрузка начальных данных
            personform = PersonForm(initial={'phone': person.phone, 'address': person.address, })
            return render(request, "person/edit.html", {"form": personform})
    except Department.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
@group_required("Managers")
def person_read(request, id):
    try:
        person = Person.objects.get(id=id) 
        return render(request, "person/read.html", {"person": person})
    except Groups.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def news_index(request):
    #news = News.objects.all().order_by('surname', 'name', 'patronymic')
    #return render(request, "news/index.html", {"news": news})
    news = News.objects.all().order_by('-daten')
    return render(request, "news/index.html", {"news": news})

# Список для просмотра
def news_list(request):
    news = News.objects.all().order_by('-daten')
    return render(request, "news/list.html", {"news": news})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def news_create(request):
    if request.method == "POST":
        news = News()        
        news.daten = request.POST.get("daten")
        news.title = request.POST.get("title")
        news.details = request.POST.get("details")
        if 'photo' in request.FILES:                
            news.photo = request.FILES['photo']        
        news.save()
        return HttpResponseRedirect(reverse('news_index'))
    else:        
        #newsform = NewsForm(request.FILES, initial={'daten': datetime.datetime.now().strftime('%Y-%m-%d'),})
        newsform = NewsForm(initial={'daten': datetime.datetime.now().strftime('%Y-%m-%d'), })
        return render(request, "news/create.html", {"form": newsform})

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
@login_required
@group_required("Managers")
def news_edit(request, id):
    try:
        news = News.objects.get(id=id) 
        if request.method == "POST":
            news.daten = request.POST.get("daten")
            news.title = request.POST.get("title")
            news.details = request.POST.get("details")
            if "photo" in request.FILES:                
                news.photo = request.FILES["photo"]
            news.save()
            return HttpResponseRedirect(reverse('news_index'))
        else:
            # Загрузка начальных данных
            newsform = NewsForm(initial={'daten': news.daten.strftime('%Y-%m-%d'), 'title': news.title, 'details': news.details, 'photo': news.photo })
            return render(request, "news/edit.html", {"form": newsform})
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def news_delete(request, id):
    try:
        news = News.objects.get(id=id)
        news.delete()
        return HttpResponseRedirect(reverse('news_index'))
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def news_read(request, id):
    try:
        news = News.objects.get(id=id) 
        return render(request, "news/read.html", {"news": news})
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Регистрационная форма 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            #print(user.id)
            # Добавить профиль
            person = Person.objects.all().order_by("-id")[0]
            id = person.id + 1            
            person = Person()
            person.id = id
            person.user = user
            person.phone = "Введите контактный телефон"
            person.address = "Введите адрес проживания"
            person.save()
            #print(person)
            #print(person.id)            
            return redirect('person_edit')
            #return redirect('index')
            #return render(request, 'registration/register_done.html', {'new_user': user})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Изменение данных пользователя
@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('index')
    #success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user
