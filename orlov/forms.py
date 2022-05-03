from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput
from .models import Position, Employee, Application, Movement, Person, News
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# При разработке приложения, использующего базу данных, чаще всего необходимо работать с формами, которые аналогичны моделям.
# В этом случае явное определение полей формы будет дублировать код, так как все поля уже описаны в модели.
# По этой причине Django предоставляет вспомогательный класс, который позволит вам создать класс Form по имеющейся модели
# атрибут fields - указание списка используемых полей, при fields = '__all__' - все поля
# атрибут widgets для указания собственный виджет для поля. Его значением должен быть словарь, ключами которого являются имена полей, а значениями — классы или экземпляры виджетов.

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={"size":"100"}),            
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('surname', 'name', 'patronymic', 'sex', 'birthday', 'address', 'phone', 'position')
        widgets = {
            'surname': TextInput(attrs={"size":"100"}),
            'name': TextInput(attrs={"size":"100"}),
            'patronymic': TextInput(attrs={"size":"100"}),
            'birthday': DateInput(attrs={"type":"date"}),
            'address': TextInput(attrs={"size":"50"}),
            'phone': TextInput(attrs={"size":"50", "type":"tel"}),            
            'position': forms.Select(attrs={'class': 'chosen'}),            
        }
        labels = {
            'position': _('position'),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('title', 'details')
        widgets = {
            'title': TextInput(attrs={"size":"100"}),
            'details': Textarea(attrs={'cols': 100, 'rows': 10}),            
        }        

class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ('datem', 'status', 'details', 'employee')
        widgets = {
            'datem': DateInput(attrs={"type":"date", "readonly":"readonly"}),
            'status': TextInput(attrs={"size":"100"}),
            'details': Textarea(attrs={'cols': 100, 'rows': 10}),
            'employee': forms.Select(attrs={'class': 'chosen'}),
        }
        labels = {
            'employee': _('employee'), 
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('phone', 'address')
        widgets = {
            'phone': TextInput(attrs={"size":"60", "type":"tel"}),            
            'address': TextInput(attrs={"size":"100"}),            
        }
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('daten', 'title', 'details', 'photo')
        widgets = {
            'daten': DateInput(attrs={"type":"date"}),
            'title': TextInput(attrs={"size":"100"}),
            'details': Textarea(attrs={'cols': 80, 'rows': 10}),            
        }

# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

