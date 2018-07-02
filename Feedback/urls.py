from . import views
from django.conf.urls import url

urlpatterns=[
	url(r'^Login',views.login),
	url(r'^Register',views.register),
]
