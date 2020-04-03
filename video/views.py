from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = 'video/main_list.html'
    context_object_name = 'videos'


class VideoDetailView(DetailView):
    model = Video


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'video', 'description']
    template_name = 'video/video_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = '/'
    template_name = 'video/video_delete.html'

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False
