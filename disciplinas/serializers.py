from rest_framework import serializers
from .models import Course, Subject

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['url_course_name', 'display_course_name', 'number_of_semesters', 'description']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['url_subject_name','display_subject_name', 'semester', 'description', 'course']
        