from django.shortcuts import render, redirect
from django.contrib import messages
# from django.http import HttpResponseRedirect
from .forms import CreateStudentForm, CreateTeacherForm, NewTerm, NewExam
from .models import Subject, Student, Teacher, Stream, Darasa, Examination


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
            messages.success(request, "Reqistered successfully")
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
            messages.success(request, "Reqistered successfully nice!")
            return redirect('exams:index')
    context = {'form': form}
    return render(request, 'exams/teacher_registration.html', context)


def term_creation(request):
    if request.method != 'POST':
        form = NewTerm()
    else:
        form = NewTerm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reqistered successfully nice!")
            return redirect('exams:index')
    context = {'form': form}
    return render(request, 'exams/new_term.html', context)


def student_profile_page(request, adm_no):
    student = Student.objects.get(adm=adm_no)
    context = {'student': student}
    return render(request, "exams/student_profile.html", context)


def teacher_profile_page(request, t_id):
    teacher = Teacher.objects.get(tch_id=t_id)
    context = {'teacher': teacher}
    return render(request, "exams/teacher_profile.html", context)


def all_students(request):
    streams = Stream.objects.all()
    darasas = Darasa.objects.all()
    context = {'streams': streams, 'darasas': darasas}
    return render(request, 'exams/students.html', context)


def all_teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'exams/teachers.html', context)


def student_class_list(request, daro_id):
    darasa = Darasa.objects.get(pk=daro_id)
    students = Student.objects.all().filter(darasa=darasa)
    context = {'darasa': darasa, 'students': students}
    return render(request, 'exams/daro_list.html', context)


def create_exam(request):
    if request.method != 'POST':
        form = NewExam()
    else:
        form = NewExam(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reqistered successfully nice!")
            return redirect('exams:index')
    context = {'form': form}
    return render(request, 'exams/create_exam.html', context)


def exams_page(request):
    exams = Examination.objects.all()
    context = {'exams': exams}
    return render(request, 'exams/exams_page.html', context)
