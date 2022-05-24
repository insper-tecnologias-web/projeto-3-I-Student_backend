from django.db import models

# Create your models here.

class Course(models.Model):
    url_course_name = models.CharField(max_length=50, unique=True)
    display_course_name = models.CharField(max_length=50, unique=True)
    number_of_semesters = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.url_course_name
    
class Subject(models.Model):
    url_subject_name = models.CharField(max_length=50, unique=True)
    display_subject_name = models.CharField(max_length=50, unique=True)
    semester = models.IntegerField()
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.url_subject_name