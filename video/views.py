from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Video
from .forms import CommentForm


class VideoListView(ListView):
    model = Video
    template_name = 'video/main_list.html'
    context_object_name = 'videos'
    paginate_by = 5


class VideoDetailView(DetailView):
    model = Video


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'video', 'description']
    template_name = 'video/video_add.html'

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


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'video/video_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False


class UserVideoView(ListView):
    model = Video
    template_name = 'video/user_list.html'
    context_object_name = 'videos'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Video.objects.filter(author=user)


@login_required
def comments_view(request, pk):
    """Funkcja oparta na: https://djangocentral.com/creating-comments-system-with-django/"""
    video = get_object_or_404(Video, pk=pk)
    comments = video.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.video = video
            new_comment.username = request.user
            new_comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'video/video_comments.html', {'video': video,
                                                         'comments': comments,
                                                         'form': form})
