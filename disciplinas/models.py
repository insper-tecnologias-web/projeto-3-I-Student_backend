from django.db import models
from django.contrib.auth.models import User

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
    
class Subject(models.Model):
    url_subject_name = models.CharField(max_length=50, unique=True)
    display_subject_name = models.CharField(max_length=50, unique=True)
    semester = models.IntegerField()
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.url_subject_name

class Summary(models.Model):
    filename = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.filename