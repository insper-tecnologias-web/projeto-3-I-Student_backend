from fileinput import filename
from tokenize import group
from django.http import HttpResponse, Http404, HttpResponseForbidden, JsonResponse

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Course, Subject, Summary
from django.contrib.auth.models import User, Group
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
def api_subject(request, course, subject):
    try:
        subject_obj = Subject.objects.get(url_subject_name=subject)
    except Subject.DoesNotExist:
        raise HttpResponse('deu merda')
    
    serialize = SubjectSerializer(subject_obj)
    return Response(serialize.data)

@api_view(['GET'])
def api_subjects_list(request, course):
    try:
        course_obj = Course.objects.get(url_course_name=course)
        subjects_list = Subject.objects.filter(course=course_obj)
        serialized_subjects = dict()
        for semester in range(course_obj.number_of_semesters):
            this_semester_subjects = list()
            for subject in subjects_list:
                if subject.semester -1 == semester:
                    this_semester_subjects.append([subject.display_subject_name, subject.url_subject_name])
            serialized_subjects[semester] = this_semester_subjects

    except Course.DoesNotExist:
        raise Http404()
    
    return JsonResponse(serialized_subjects)
    

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

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_post_summary(request, course, subject):
    try:
        course_obj = Course.objects.get(url_course_name=course)
        subject_obj = Subject.objects.get(url_subject_name=subject)
        summary_data = request.data
        # filename = summary_data['filename']
        file = summary_data['file']
        print(file)
        if(len(file)!=0):
            new_summary = Summary.objects.create(subject=subject_obj, filename=file.name, file=file)
            deuCerto = True
        else:
            deuCerto = False
            
    except Course.DoesNotExist or Subject.DoesNotExist:
        raise Http404()
    
    return JsonResponse({'deuCerto': deuCerto})
    
@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            print(User.objects.all())
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()

@api_view(['POST'])
def api_create_account(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']

            group = Group.objects.get(name='aluno')
            print(group)
            
            user, created = User.objects.get_or_create(username=username)
            user.set_password(password)
            user.groups.add(group)
            user.save()
            
    except:
        raise Http404()
    
    return JsonResponse({'created': created})
