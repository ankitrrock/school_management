from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from account.models import Depthead, Student, Teacher, Staff, User

class DeptheadSignupForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required = True)
      
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self):
        user = super().save(commit = False)
        user.is_depthead = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        depthead= Depthead.objects.create(user=user)
        depthead.phone_number = self.cleaned_data.get("phone_number")
        depthead.location = self.cleaned_data.get("location")
        depthead.save()
        return Depthead
        
class TeacherSignupForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    designation = forms.CharField(required = True)
    
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self):
        user = super().save(commit = False)
        user.is_teacher = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        teacher= Teacher.objects.create(user=user)
        teacher.phone_number = self.cleaned_data.get("phone_number")
        teacher.designation = self.cleaned_data.get("designation")
        teacher.save()
        return Teacher

class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    branch = forms.CharField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit = False)
        user.is_student = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        student= Student.objects.create(user=user)
        student.phone_number = self.cleaned_data.get("phone_number")
        student.branch = self.cleaned_data.get("branch")
        student.save()
        return Student

class StaffSignupForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    area = forms.CharField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit = False)
        user.is_staff = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        staff= Staff.objects.create(user=user)
        staff.phone_number = self.cleaned_data.get("phone_number")
        staff.area = self.cleaned_data.get("area")
        staff.save()
        return Staff