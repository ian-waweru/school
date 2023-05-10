from django.db import models


# Create your models here.


class Stream(models.Model):
    stream_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Darasa(models.Model):
    daro_id = models.AutoField(primary_key=True, default=None)
    daro_name = models.CharField(max_length=15)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stream} {self.daro_name}'


class Student(models.Model):
    """Student information"""
    adm = models.IntegerField(unique=True, default=None)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    male = 'm'
    female = 'f'
    GENDER_CHOICES = [
        (male, 'MALE'),
        (female, 'FEMALE'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1, null=False, default=None)
    birthday = models.DateField(null=True, blank=True)
    darasa = models.ForeignKey(Darasa, null=True, on_delete=models.SET_NULL)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Teacher(models.Model):
    tch_id = models.AutoField(primary_key=True, default=None)
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    tsc_no = models.IntegerField(default=None)
    telephone = models.IntegerField(null=True)
    email = models.EmailField(max_length=20, null=True)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('ENGLISH', 'ENGLISH'),
        ('KISWAHILI', 'KISWAHILI'),
        ('MATHEMATICS', 'MATHEMATICS'),
        ('BIOLOGY', 'BIOLOGY'),
        ('PHYSICS', 'PHYSICS'),
        ('CHEMISTRY', 'CHEMISTRY'),
        ('HISTORY', 'HISTORY'),
        ('GEOGRAPHY', 'GEOGRAPHY'),
        ('CRE', 'CRE'),
        ('BS', 'BUSINESS STUDIES'),
        ('AGRICULTURE','AGRICULTURE'),
    ]
    sub_name = models.CharField(choices=SUBJECT_CHOICES, max_length=15, null=False, blank=False)
    teacher = models.ForeignKey(Teacher, default=None, blank=False, null=True, on_delete=models.SET_DEFAULT)
    darasa = models.ForeignKey(Darasa, default=None, blank=True, null=True, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f'{self.darasa} {self.sub_name}'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True, default=None)
    f_name = models.CharField(max_length=15)
    s_name = models.CharField(max_length=15)


class Department(models.Model):
    dpt_id = models.AutoField(primary_key=True, default=None)
    dpt_name = models.CharField(max_length=15)


class Term(models.Model):
    # term choices should come from existing term as below
    term_choices = [
        (None, 'Pick Term'),
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three')
    ]
    name = models.IntegerField(choices=term_choices, null=False, default=None)
    start_date = models.DateField()
    closing_date = models.DateField()

    def __str__(self):
        return f'Term {self.name}'


class Examination(models.Model):
    name = models.CharField(max_length=55)
    start_date = models.DateField()
    end_date = models.DateField()

    # no need for the exam attribute below since a term cannot be deleted once done
    # can be determined by a function that determines whether  the start date of the exam is within the term dates

    def set_term(self):
        terms = Term.objects.all()
        for term in terms:
            if term.start_date < Examination.start_date < term.end_date:
                self.term = term


class ExamResult(models.Model):
    """ The exact score scored by a student in a subject in that particular exam """
    exam = models.ForeignKey(Examination, null=False, on_delete=models.CASCADE, default=None)
    student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE, default=None)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    score = models.IntegerField(default=None)
