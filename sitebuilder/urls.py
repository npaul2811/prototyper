
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<slug>[\w./-]+)$', views.page, name='page'),
	url(r'^$', views.page, name='homepage'),
]