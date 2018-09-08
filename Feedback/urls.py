from django.urls import path
from . import views

urlpatterns = [
    path('feedback/<str:class_name>/', views.Feedback_form_Page),
]
