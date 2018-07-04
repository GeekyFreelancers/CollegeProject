from . import views
from django.conf.urls import url

urlpatterns=[
	url(r'^Login',views.login),
	#path('a/',views.a),
	url(r'^Register',views.register),
]
