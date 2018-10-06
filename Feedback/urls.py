from django.urls import path
from . import views

urlpatterns = [
    path('feedback/<str:class_name>/', views.Feedback_form_Page),
    path('', views.Feedback_submit, name='submit'),
    path('t', views.teacher_check, name='teacher_check'),
]
