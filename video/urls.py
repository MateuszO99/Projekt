from django.urls import path
from .views import (
    VideoListView,
    VideoDetailView,
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
    path('video/<int:pk>/', VideoDetailView.as_view(), name='detail'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='delete'),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name='update'),
    path('video/<int:pk>/comments/', views.comments_view, name='comments'),
    path('video/<str:username>/', UserVideoView.as_view(), name='user-list'),
]
