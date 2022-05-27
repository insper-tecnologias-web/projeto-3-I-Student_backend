from django.http import HttpResponse, Http404, HttpResponseForbidden, JsonResponse

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

@api_view(['GET'])
def api_summarys(request, course, subject):
    try:
        course_obj = Course.objects.get(url_course_name=course)
        subject_obj = Subject.objects.get(url_subject_name=subject)
        summary_list = Summary.objects.filter(subject=subject_obj)
    except Course.DoesNotExist or Subject.DoesNotExist:
        raise Http404()
    
    serialized_summarys = SummarySerializer(summary_list, many=True)
    return Response(serialized_summarys.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_post_summary(request, course, subject):
    try:
        course_obj = Course.objects.get(url_course_name=course)
        subject_obj = Subject.objects.get(url_subject_name=subject)

    except Course.DoesNotExist or Subject.DoesNotExist:
        raise Http404()
    
    return HttpResponse('oi!')
    
@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()
