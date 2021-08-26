from django.urls import path
from django.urls.resolvers import URLPattern

from .views import post_list

urlpatterns = [
    path('post_list/', post_list, name='post_list'),
]