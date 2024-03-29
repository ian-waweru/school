from django.urls import path
from . import views

"""Defines URL patterns for exams"""
app_name = 'exams'
urlpatterns = [
    path('', views.index, name='index'),
    path('studentregistration/', views.student_registration, name='stud_reg'),
    path('teacherregistration/', views.teacher_registration, name="teacher_reg"),
    path('createterm/', views.term_creation, name='create_term'),
    path('studentprofile/<adm_no>/', views.student_profile_page, name='profiler'),
    path('teacherprofile/<t_id>/', views.teacher_profile_page, name="t_profile"),
    path('studentlist/', views.all_students, name='allstudents'),
    path('teacherlist/', views.all_teachers, name='allteachers'),
    path('classlist/<int:daro_id>/', views.student_class_list, name='class_list'),
    path('createexam/', views.create_exam, name='create_exam'),
    path('examlist/', views.exams_page, name='exams_list'),
]