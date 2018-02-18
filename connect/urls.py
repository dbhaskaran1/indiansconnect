from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_site, name='view_site'),
    url(r'^aboutus$', views.aboutus, name='aboutus'),
]
