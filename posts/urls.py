# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name='post_list'),
    path('<int:id>/', views.detail_post, name='post_detail'),
    path('new/', views.new_post, name='post_new'),
    path('<int:id>/delete/', views.delete_post, name='post_delete'),
]
