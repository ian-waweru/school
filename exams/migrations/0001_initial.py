# Generated by Django 4.0.5 on 2023-03-24 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Darasa',
            fields=[
                ('daro_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('daro_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dpt_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('dpt_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=15)),
                ('s_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('stream_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=15)),
                ('darasa', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='exams.darasa')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(None, 'Pick Term'), (1, 'One'), (2, 'Two'), (3, 'Three')], default=None)),
                ('start_date', models.DateField()),
                ('closing_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tch_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=15)),
                ('l_name', models.CharField(max_length=15)),
                ('tsc_no', models.IntegerField(default=None)),
                ('telephone', models.BigIntegerField(null=True)),
                ('email', models.EmailField(max_length=20, null=True)),
                ('subjects', models.ManyToManyField(to='exams.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm', models.IntegerField(default=None, unique=True)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[(None, 'Choose Gender:'), ('m', 'MALE'), ('f', 'FEMALE')], default=None, max_length=1)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('darasa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.darasa')),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('term', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exams.term')),
            ],
        ),
        migrations.AddField(
            model_name='darasa',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.stream'),
        ),
    ]