from django.contrib import admin
from exams.models import Student, Teacher, Subject, Staff, Department, Stream, Darasa, Term, Examination, ExamResult


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["adm", "f_name", "l_name", "darasa"]
    search_fields = ["adm", "f_name", "l_name", "darasa"]
    list_per_page = 10


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Stream)
admin.site.register(Darasa)
admin.site.register(Term)
admin.site.register(Examination)
admin.site.register(ExamResult)