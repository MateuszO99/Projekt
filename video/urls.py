from django.urls import path
from .views import (
    VideoListView,
    VideoDetailView,
    VideoCreateView,
    VideoDeleteView,
)

app_name = 'video'

urlpatterns = [
    path('', VideoListView.as_view(), name='main_list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='detail'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='delete'),
    path('video/create/', VideoCreateView.as_view(), name='create'),
]
