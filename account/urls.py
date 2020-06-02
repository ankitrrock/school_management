from django.urls import path
from account import views as accdata


urlpatterns = [
	path('',accdata.register, name='register'),
    path('index/',accdata.index, name='index'),
    path('depthead_register/',accdata.depthead_register.as_view(), name='depthead_register'),
    path('teacher_register/',accdata.teacher_register.as_view(), name='teacher_register'),
	path('student_register/',accdata.student_register.as_view(), name='student_register'),
    path('staff_register/',accdata.staff_register.as_view(), name='staff_register'),
    path('login/',accdata.login_request, name='login'),
    path('logout/',accdata.logout_view, name='logout'),
]