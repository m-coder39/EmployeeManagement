# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from employees.forms import EmployeeForm
from employees.forms import LoginForm
from employees.forms import SignupForm
from employees.models import CustomUser
from employees.models import Employee


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Register(View):
    def post(self, request):
        form_instance = SignupForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('employees:Employeelogin')
        return render(request, "register.html", {"form": form_instance})

    def get(self, request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, "register.html", context)


class Employeelogin(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            u = data['username']
            p = data['password']
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
                return redirect('employees:Home')
            else:
                messages.error(request, 'Invalid user credentials')
                return redirect('employees:Employeelogin')

    def get(self, request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request, "Employeelogin.html", context)


class Employeelogout(View):
    def get(self, request):
        logout(request)
        return redirect("employees:Employeelogin")


class Viewemployees(View):
    def get(self, request):
        b = CustomUser.objects.all()
        print(b)
        return render(request, "viewemployees.html", {'employees': b})


class Search(View):
    def get(self, request):
        query = request.GET['q']
        print(query)
        b = CustomUser.objects.filter(Q(name__icontains=query) |
                                      Q(deptname__icontains=query) |
                                      Q(salary__icontains=query) |
                                      Q(designation__icontains=query))
        context = {'employees': b, 'query': query}
        return render(request, 'search.html', context)


class Detail(View):
    def get(self, request, i):
        b = CustomUser.objects.get(id=i)
        context = {'employee': b}
        return render(request, "detail.html", context)


class Edit(View):
    def post(self, request, i):
        b = CustomUser.objects.get(id=i)
        form_instance = EmployeeForm(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('employees:Viewemployees')

    def get(self, request, i):
        b = CustomUser.objects.get(id=i)
        form_instance = EmployeeForm(instance=b)
        context = {'form': form_instance}
        return render(request, "edit.html", context)


class Delete(View):
    def get(self, request, i):
        b = CustomUser.objects.get(id=i)
        b.delete()
        return redirect('employees:Viewemployees')
