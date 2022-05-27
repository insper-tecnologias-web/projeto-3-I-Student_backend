from django.http import HttpResponse
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course, Subject, Summary
from .serializers import CourseSerializer, SubjectSerializer, SummarySerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET'])
def api_courses(request):
    try:
        course_list = Course.objects.all()
    except Course.DoesNotExist:
        raise Http404()
    
    serialized_courses = CourseSerializer(course_list, many=True)
    return Response(serialized_courses.data)

@api_view(['GET'])
def api_subjects(request, course):
    try:
        course_obj = Course.objects.get(url_course_name=course)
        subjects_list = Subject.objects.filter(course=course_obj)
    except Course.DoesNotExist:
        raise Http404()
    
    serialized_subjects = SubjectSerializer(subjects_list, many=True)
    return Response(serialized_subjects.data)

@api_view(['GET', 'POST'])
def api_summarys(request, course, subject):
    try:
        course_obj = Course.objects.get(url_course_name=course)
        subject_obj = Subject.objects.get(url_subject_name=subject)
        summary_list = Summary.objects.filter(subject=subject_obj)
    except Course.DoesNotExist or Subject.DoesNotExist:
        raise Http404()
    
    serialized_summarys = SummarySerializer(summary_list, many=True)
    return Response(serialized_summarys.data)