from .models import Student, Teacher, Examination, Subject, Term, Darasa
from django import forms
from django.core.validators import RegexValidator


class CreateStudentForm(forms.ModelForm):
    adm = forms.IntegerField(
        label='Admission Number',
        help_text="As it appears on ID",
        # Strip: THe value will be stripped of leading and trailing whitespaces
        # strip=True,
        # validators=[RegexValidator(r'^[]*$', message="Only letters allowed!")],
        widget=forms.NumberInput(attrs={'placeholder': 'Admission No'})
    )

    f_name = forms.CharField(
        label='First Name', min_length=3, max_length=50,
        help_text="As it appears on ID",
        # Strip: THe value will be stripped of leading and trailing whitespaces
        # strip=True,
        # validators=[RegexValidator(r'^[]*$', message="Only letters allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    l_name = forms.CharField(
        label='Last Name', min_length=3, max_length=50,
        help_text="As it appears on ID",
        # Strip: THe value will be stripped of leading and trailing whitespaces
        # strip=True,
        # validators=[RegexValidator(r'^[]*$', message="Only letters allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    gender = forms.ChoiceField(
        choices=Student.GENDER_CHOICES,
        label='Gender',
        help_text="As it appears on ID",
        # Strip: THe value will be stripped of leading and trailing whitespaces
        # strip=True,
        # validators=[RegexValidator(r'^[]*$', message="Only letters allowed!")],
        widget=forms.RadioSelect(attrs={'placeholder': 'Gender', 'class': 'form-control'})
    )

    birthday = forms.CharField(
        label='Date of birth',
        help_text="Enter birth date",
        # Strip: THe value will be stripped of leading and trailing whitespaces
        # strip=True,
        # validators=[RegexValidator(r'^[]*$', message="Only letters allowed!")],
        widget=forms.DateInput(attrs={'placeholder': 'Birth date', 'type': 'date'})
    )

    darasa = forms.ModelChoiceField(
        label='Class',
        queryset=Darasa.objects.all(),
        help_text="Enter class to be admitted",
        widget=forms.Select(attrs={'placeholder': 'Class admitted', 'class': 'form-control'})
    )

    class Meta:
        model = Student

        fields = '__all__'
        # fields = ['adm', 'f_name', 'l_name', 'gender', 'birthday', 'darasa']
        # labels = {'adm': 'Admission number', 'f_name': 'First Name', 'l_name': 'Last Name', 'gender': 'Gender',
        #          'birthday': 'Date of Birth', 'darasa': 'Class admitted'}
        # widgets = {
        #    'birthday': forms.DateInput(attrs={'type': 'date'})
        # }


class CreateTeacherForm(forms.ModelForm):
    f_name = forms.CharField(
        label='First Name', min_length=3, max_length=50,
        help_text="As it appears on ID",
        # Strip: THe value will be stripped of leading and trailing whitespaces
        strip=True,
        # validators=[RegexValidator(r'^[]*$', message="Only letters allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    l_name = forms.CharField(
        label='Last Name', min_length=3, max_length=50,
        help_text="As it appears on ID",
        # validators=[RegexValidator(r'^[a-zA-Z]*$', message="Only letters allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    tsc_no = forms.CharField(
        label='TSC Number', min_length=6, max_length=10,
        # validators=[RegexValidator(r'^[a-zA-Z]*$', message="Only letters allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'TSC'})
    )

    email = forms.CharField(
        label='Email Address', min_length=3, max_length=50,
        # validators=[RegexValidator(r'^[a-zA-Z]*$', message="Only letters allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'name@example.com'})
    )

    telephone = forms.CharField(
        label='Phone Number', min_length=8, max_length=15,
        # validators=[RegexValidator(regex=r'^[0-9]*$', message="Only numbers allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'Phone'})
    )

    class Meta:
        model = Teacher

        fields = '__all__'
        # fields = ['f_name', 'l_name', 'tsc_no', 'telephone', 'email']


class NewTerm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=Term.term_choices,
        label='Enter Term',
        # validators=[RegexValidator(r'^[a-zA-Z]*$', message="Only letters allowed!")],
        widget=forms.Select(attrs={'placeholder': 'eg, Term One', 'class': 'form-control'})
    )

    start_date = forms.DateField(
        label='Start Date',
        # validators=[RegexValidator(r'^[a-zA-Z]*$', message="Only letters allowed!")],
        widget=forms.DateInput(attrs={'placeholder': 'Start', 'type': 'date'})
    )

    closing_date = forms.DateField(
        label='Closing Date',
        # validators=[RegexValidator(regex=r'^[0-9]*$', message="Only numbers allowed!")],
        widget=forms.DateInput(attrs={'placeholder': 'Closing', 'type': 'date'})
    )

    class Meta:
        model = Term

        fields = '__all__'
        #  fields = ['name','start_date','closing_date']


class NewExam(forms.ModelForm):
    name = forms.CharField(
        label='Exam Name',
        # validators=[RegexValidator(r'^[a-zA-Z]*$', message="Only letters allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'eg, Opener', 'class': 'form-control'})
    )

    start_date = forms.DateField(
        label='Start Date',
        # validators=[RegexValidator(r'^[a-zA-Z]*$', message="Only letters allowed!")],
        widget=forms.DateInput(attrs={'placeholder': 'Start', 'type': 'date'})
    )

    closing_date = forms.DateField(
        label='Closing Date',
        # validators=[RegexValidator(regex=r'^[0-9]*$', message="Only numbers allowed!")],
        widget=forms.DateInput(attrs={'placeholder': 'Closing', 'type': 'date'})
    )

    class Meta:
        model = Examination

        fields = '__all__'
        #  fields = ['name','start_date','closing_date']
