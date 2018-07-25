from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/$', views.index),
	# url(r'^login/$', views.user_login),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
	url(r'^logout-then-login/$', 'django.contrib.views.logout_then_login')
]