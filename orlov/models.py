from django.db import models
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

# Модели отображают информацию о данных, с которыми вы работаете.
# Они содержат поля и поведение ваших данных.
# Обычно одна модель представляет одну таблицу в базе данных.
# Каждая модель это класс унаследованный от django.db.models.Model.
# Атрибут модели представляет поле в базе данных.
# Django предоставляет автоматически созданное API для доступа к данным
# choices (список выбора). Итератор (например, список или кортеж) 2-х элементных кортежей,
# определяющих варианты значений для поля.
# При определении, виджет формы использует select вместо стандартного текстового поля
# и ограничит значение поля указанными значениями.

# Create your models here.
# Должности 
class Position(models.Model):
    # Читабельное имя поля (метка, label). Каждое поле, кроме ForeignKey, ManyToManyField и OneToOneField,
    # первым аргументом принимает необязательное читабельное название.
    # Если оно не указано, Django самостоятельно создаст его, используя название поля, заменяя подчеркивание на пробел.
    # null - Если True, Django сохранит пустое значение как NULL в базе данных. По умолчанию - False.
    # blank - Если True, поле не обязательно и может быть пустым. По умолчанию - False.
    # Это не то же что и null. null относится к базе данных, blank - к проверке данных.
    # Если поле содержит blank=True, форма позволит передать пустое значение.
    # При blank=False - поле обязательно.
    title = models.CharField(_('position_title'), unique=True, max_length=64)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'position'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод Название в тег SELECT 
        return self.title

# Сотрудники
class Employee(models.Model):
    SEX_CHOICES = (
        ('М','М'),
        ('Ж', 'Ж'),
    )
    surname = models.CharField(_('surname'), max_length=64)
    name = models.CharField(_('name'), max_length=64)
    patronymic = models.CharField(_('patronymic'), max_length=64, blank=True, null=True)    
    sex = models.CharField(_('sex'), max_length=1, choices=SEX_CHOICES, default='М')
    birthday = models.DateTimeField(_('birthday'))
    address = models.CharField(_('address'), max_length=128, blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=128, blank=True, null=True)
    position = models.ForeignKey(Position, related_name='employee_position', on_delete=models.CASCADE)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'employee'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['surname']),
            models.Index(fields=['name']),
            models.Index(fields=['patronymic']),
            models.Index(fields=['position']),
        ]
        # Сортировка по умолчанию
        ordering = ['surname', 'name', 'patronymic']
    def __str__(self):
        # Вывод ФИО в тег SELECT 
        return "{} {} {}".format(self.surname, self.name, self.patronymic)
        # Override the save method of the model
    @property
    def fio(self):
        # Возврат ФИО
        return '%s %s %s' % (self.surname, self.name, self.patronymic)

# Заявка клиента
class Application(models.Model):
    datea = models.DateTimeField(_('datea'), auto_now_add=True)
    user = models.ForeignKey(User, related_name='application_user', on_delete=models.CASCADE)
    title = models.CharField(_('application_title'), max_length=255)
    details = models.TextField(_('application_details'))
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'application'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['datea']),
            models.Index(fields=['user']),
        ]
        # Сортировка по умолчанию
        ordering = ['datea']
    def __str__(self):
        # Вывод в тег Select
        return "{} ({}): {}".format(self.datea.strftime('%d.%m.%Y'), self.user, self.title)

# Рассмотрение заявки клиента
class Movement(models.Model):
    application = models.ForeignKey(Application, related_name='movement_application', on_delete=models.CASCADE)
    datem = models.DateTimeField(_('datem'))
    status = models.CharField(_('movement_status'), max_length=128)
    details = models.TextField(_('movement_details'), blank=True, null=True)
    employee = models.ForeignKey(Employee, related_name='movement_employee', on_delete=models.CASCADE)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'movement'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['application']),
            models.Index(fields=['datem']),
            models.Index(fields=['employee']),
        ]
        # Сортировка по умолчанию
        ordering = ['datem']        
    def __str__(self):
        # Вывод в тег Select
        return "{} ({}): {}".format(self.datem.strftime('%d.%m.%Y'), self.application, self.status)

# Персона (Клиент)
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(_('phone'), max_length=64)
    address = models.CharField(_('address'), max_length=128)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'person'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['phone']),            
        ]
        # Сортировка по умолчанию
        ordering = ['phone']        
    def __str__(self):
        # Вывод в тег Select
        return "{} {} ({})".format(self.user.first_name, self.last_name, self.user.eamil)
    
# Новости 
class News(models.Model):
    daten = models.DateTimeField(_('daten'))
    title = models.CharField(_('title_news'), max_length=256)
    details = models.TextField(_('details_news'))
    photo = models.ImageField(_('photo_news'), upload_to='images/', blank=True, null=True)    
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'news'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['daten']),
        ]
        # Сортировка по умолчанию
        ordering = ['daten']


