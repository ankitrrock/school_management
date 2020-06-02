from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import DeptheadSignupForm, TeacherSignupForm, StudentSignupForm, StaffSignupForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request, 'register.html')

class depthead_register(CreateView):
    model = User
    form_class = DeptheadSignupForm
    template_name = 'depthead_register.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('depthead_register')

class teacher_register(CreateView):
    model = User
    form_class = TeacherSignupForm
    template_name = 'teacher_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class student_register(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class staff_register(CreateView):
    model = User
    form_class = StaffSignupForm
    template_name = 'staff_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html', context={'form':AuthenticationForm()})
@login_required(login_url=login)
def logout_view(request):
    logout(request)
    return redirect('/')
def index(request):

    return render(request, 'index.html')