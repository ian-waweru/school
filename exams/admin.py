from django.contrib import admin
from exams.models import Student, Teacher, Subject, Staff, Department, Stream, Darasa, Term, Examination

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Stream)
admin.site.register(Darasa)
admin.site.register(Term)
admin.site.register(Examination)