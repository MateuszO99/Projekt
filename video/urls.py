from django.urls import path
from .views import (
    VideoListView,
    VideoDetailView,
)

urlpatterns = [
    path('', VideoListView.as_view(), name='main_list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
]
