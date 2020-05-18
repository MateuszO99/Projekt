from django.urls import path
from .views import (
    VideoListView,
    VideoCreateView,
    VideoDeleteView,
    VideoUpdateView,
    UserVideoView,
)
from . import views

app_name = 'video'

urlpatterns = [
    path('', VideoListView.as_view(), name='main_list'),
    path('video/create/', VideoCreateView.as_view(), name='create'),
    path('video/<int:pk>/', views.video_detail_view, name='detail'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='delete'),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name='update'),
    path('video/<int:pk>/comments/', views.comments_view, name='comments'),
    path('video/<int:pk>/favourite/', views.favourite_view, name='favourite'),
    path('video/favourite/', views.favourite_list_view, name='favourite_list'),
    path('video/<int:pk>/to_watch/', views.to_watch_view, name='to_watch'),
    path('video/to_watch/', views.to_watch_list_view, name='watch_list'),
    path('video/like/', views.like_video, name='like_video'),
    path('video/dislike/', views.dislike_video, name='dislike_video'),
    path('video/<str:username>/', UserVideoView.as_view(), name='user-list'),
]
