from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('details/', views.details, name='details'),
    re_path('listing/', views.list, name='list'),
]