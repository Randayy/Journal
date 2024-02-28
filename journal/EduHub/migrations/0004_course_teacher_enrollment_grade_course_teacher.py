# Generated by Django 5.0.2 on 2024-02-28 15:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduHub', '0003_remove_student_id_alter_student_stud_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('fullname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(6, 'the field must contain at least 6 characters')])),
                ('subject', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollmer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='EduHub.course')),
                ('student', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='EduHub.student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('grade_id', models.IntegerField(primary_key=True, serialize=False)),
                ('grade', models.IntegerField(max_length=3)),
                ('date', models.DateField()),
                ('course', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='EduHub.course')),
                ('student', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='EduHub.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(db_column='teacher_id', on_delete=django.db.models.deletion.CASCADE, to='EduHub.teacher'),
        ),
    ]
