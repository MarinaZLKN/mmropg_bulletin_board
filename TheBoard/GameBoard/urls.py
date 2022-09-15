from django.urls import path
from .views import PostList, PostDetail, PostCreate
from django import views

urlpatterns = [
    path('posts/', PostList.as_view(), name='home'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),

]