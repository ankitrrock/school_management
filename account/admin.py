from django.contrib import admin
from account.models import User, Teacher, Depthead, Student, Staff
# Register your models here.

admin.site.register(Depthead)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(User)