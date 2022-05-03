"""repair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings 
from django.conf.urls.static import static 
from django.conf.urls import include

from orlov import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    #path('report/', views.report, name='report'),        
    path('admin/', admin.site.urls),
    path('signup/$', views.signup, name='signup'),
    path('i18n/', include('django.conf.urls.i18n')),

    path('person/index/', views.person_index, name='person_index'),
    #path('person/create/', views.person_create, name='person_create'),
    #path('person/edit/<int:id>/', views.person_edit, name='person_edit'),
    path('person/edit/', views.person_edit, name='person_edit'),
    #path('person/delete/<int:id>/', views.person_delete, name='person_delete'),
    path('person/read/<int:id>/', views.person_read, name='person_read'),    

    path('position/index/', views.position_index, name='position_index'),
    path('position/create/', views.position_create, name='position_create'),
    path('position/edit/<int:id>/', views.position_edit, name='position_edit'),
    path('position/delete/<int:id>/', views.position_delete, name='position_delete'),
    path('position/read/<int:id>/', views.position_read, name='position_read'),

    path('employee/index/', views.employee_index, name='employee_index'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/edit/<int:id>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('employee/read/<int:id>/', views.employee_read, name='employee_read'),

    path('application/index/', views.application_index, name='application_index'),
    path('application/list/', views.application_list, name='application_list'),
    path('application/create/', views.application_create, name='application_create'),
    path('application/edit/<int:id>/', views.application_edit, name='application_edit'),
    path('application/delete/<int:id>/', views.application_delete, name='application_delete'),
    path('application/read/<int:id>/', views.application_read, name='application_read'),

    path('movement/index/<int:application_id>/', views.movement_index, name='movement_index'),
    path('movement/create/<int:application_id>/', views.movement_create, name='movement_create'),
    path('movement/edit/<int:id>/<int:application_id>/', views.movement_edit, name='movement_edit'),
    path('movement/delete/<int:id>/<int:application_id>/', views.movement_delete, name='movement_delete'),
    path('movement/read/<int:id>/<int:application_id>/', views.movement_read, name='movement_read'),

    path('news/index/', views.news_index, name='news_index'),
    path('news/list/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/edit/<int:id>/', views.news_edit, name='news_edit'),
    path('news/delete/<int:id>/', views.news_delete, name='news_delete'),
    path('news/read/<int:id>/', views.news_read, name='news_read'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('settings/account/$', views.UserUpdateView.as_view(), name='my_account'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



