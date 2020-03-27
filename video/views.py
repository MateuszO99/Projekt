from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = 'video/main_list.html'
    context_object_name = 'videos'


class VideoDetailView(DetailView):
    model = Video
