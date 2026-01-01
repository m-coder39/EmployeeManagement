"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path

from . import views

app_name = 'employees'
urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('Register', views.Register.as_view(), name="Register"),
    path('Employeelogin', views.Employeelogin.as_view(), name="Employeelogin"),
    path('Employeelogout', views.Employeelogout.as_view(), name="Employeelogout"),
    path('Viewemployees', views.Viewemployees.as_view(), name="Viewemployees"),
    path('Search', views.Search.as_view(), name="Search"),
    path('detail/<int:i>/', views.Detail.as_view(), name='Detail'),
    path('edit/<int:i>/', views.Edit.as_view(), name='Edit'),
    path('delete/<int:i>/', views.Delete.as_view(), name='Delete'),
]
