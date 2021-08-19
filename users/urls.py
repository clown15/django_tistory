from django.urls import path
from django.urls.resolvers import URLPattern

from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
]