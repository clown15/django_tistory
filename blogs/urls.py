from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('post/list/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/write/', views.post_write, name='post_write'),
    path('comment/write/',views.comment_write, name='comment_write'),
]