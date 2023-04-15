from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .forms import CreateStudentForm, CreateTeacherForm
from .models import Subject, Student, Teacher, Stream, Darasa

from .forms import CreateStudentForm


# Create your views here.


def index(request):
    return render(request, 'exams/index.html')


def student_registration(request):
    if request.method != 'POST':
        form = CreateStudentForm()
    else:
        form = CreateStudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('exams:index')

    context = {'form': form}
    return render(request, 'exams/student_registration.html', context)


def teacher_registration(request):
    if request.method != 'POST':
        form = CreateTeacherForm()
    else:
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exams:index')
    context = {'form': form}
    return render(request, 'exams/teacher_registration.html', context)


def student_profile_page(request, adm_no):
    student = Student.objects.get(adm=adm_no)
    context = {'student': student}
    return render(request, "exams/student_profile.html", context)


def teacher_profile_page(request, t_id):
    teacher = Teacher.objects.get(tch_id=t_id)
    subjects = teacher.subjects.all()
    context = {'teacher': teacher, 'subjects': subjects}
    return render(request, "exams/teacher_profile.html", context)


def all_students(request):
    streams = Stream.objects.all()
    darasas = Darasa.objects.all()
    context = {'streams': streams, 'darasas': darasas}
    return render(request, 'exams/students.html', context)


def student_class_list(request, daro_id):
    darasa = Darasa.objects.get(pk=daro_id)
    students = Student.objects.all().filter(darasa=darasa)
    context = {'darasa': darasa, 'students': students}
    return render(request, 'exams/daro_list.html', context)
