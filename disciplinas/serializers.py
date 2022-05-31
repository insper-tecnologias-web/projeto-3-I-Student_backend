from rest_framework import serializers
from .models import Course, Semester, Subject

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('url_course_name', 'display_course_name', 'number_of_semesters', 'description', 'background_img', 'img_description')

class SemesterSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Semester
        fields = ('number_of_semester', 'display_semester_name', 'course', 'subjects')

class CourseSerializer(serializers.ModelSerializer):
    semesters = SemesterSerializer(serializers.ModelSerializer)
    class Meta:
        model = Course
        fields = ('url_subject_name', 'display_subject_name', 'semester', 'description', 'semesters')
