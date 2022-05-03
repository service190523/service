from django.contrib import admin
# Импорт модели
from .models import Position
from .models import Employee
from .models import Application
from .models import Movement
from .models import Person
from .models import News
# Добавление модели на главную страницу интерфейса администратора
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Application)
admin.site.register(Movement)
admin.site.register(Person)
admin.site.register(News)
