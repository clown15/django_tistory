from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    # path(접속할 url, 연결할 view, url이름)
    path('',views.post_list, name='home'),
    path('post/list/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/write/', views.post_write, name='post_write'),
    path('post/update/<int:post_id>/', views.post_update, name='post_update'),
    path('post/delete/<int:post_id>/',views.post_delete, name='post_delete'),
    path('comment/write/', views.comment_write, name='comment_write'),
    path('post/like/', views.post_like, name='post_like'),
]