from .models import Student, Teacher, Examination
from django import forms


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['adm', 'f_name', 'l_name', 'gender', 'birthday', 'darasa']
        labels = {'adm': 'Admission number', 'f_name': 'First Name', 'l_name': 'Last Name', 'gender': 'Gender',
                  'birthday': 'Date of Birth', 'darasa': 'Class admitted'}
        widgets = {
            'birthday': forms.DateInput(attrs= {'type': 'date'})
        }


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class ExamPerClass(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['term']

