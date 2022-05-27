from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/courses/', views.api_courses),
    path('api/<str:course>/subjects/', views.api_subjects),
    path('api/<str:course>/<str:subject>/', views.api_summarys),
    path('api/<str:course>/<str:subject>/upload/', views.api_post_summary),
    path('api/token/', views.api_get_token)
]