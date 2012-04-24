from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField("Student's first name", max_length=30)
    last_name = models.CharField("Student's last name", max_length=30)

class Teacher(models.Model):
    first_name = models.CharField("Teacher's first name", max_length=30)
    last_name = models.CharField("Teacher's last name", max_length=30)

class Course(models.Model):
    title = models.CharField("Course title", max_length=200)
    max_students = models.IntegerField()
    teacher_id = models.ForeignKey(Teacher)


class CourseRegister(models.Model):
    course_id = models.ForeignKey(Course)
    student_id = models.ForeignKey(Student)
    unique_together = ("course_id", "student_id")


import models
from django.contrib import admin

admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Course)
admin.site.register(models.CourseRegister)
    
