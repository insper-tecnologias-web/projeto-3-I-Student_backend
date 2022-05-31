from django.db import models

# Create your models here.

class Course(models.Model):
    url_course_name = models.CharField(max_length=50, unique=True)
    display_course_name = models.CharField(max_length=50, unique=True)
    number_of_semesters = models.IntegerField()
    description = models.TextField()
    background_img =  models.ImageField(upload_to = 'images/')
    img_description = models.CharField(max_length=50, default=display_course_name)

    def __str__(self):
        return self.url_course_name

class Semester(models.Model):
    number_of_semester = models.IntegerField()
    display_semester_name = models.CharField(max_length=50, default = f'{number_of_semester}° Semestre')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
class Subject(models.Model):
    url_subject_name = models.CharField(max_length=50, unique=True)
    display_subject_name = models.CharField(max_length=50, unique=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.url_subject_name
        