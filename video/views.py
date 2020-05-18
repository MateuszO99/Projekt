from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
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


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'video', 'description', 'thumbnail']
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
    fields = ['title', 'description', 'thumbnail']
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

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Video.objects.filter(author=user)


def video_detail_view(request, pk):
    video = get_object_or_404(Video, pk=pk)
    favourite = False
    to_watch = False
    like = False
    dislike = False

    if video.favourite.filter(pk=request.user.pk).exists():
        favourite = True

    if video.to_watch.filter(pk=request.user.pk).exists():
        to_watch = True

    if video.likes.filter(pk=request.user.pk).exists():
        like = True

    if video.dislikes.filter(pk=request.user.pk).exists():
        dislike = True

    return render(request, 'video/video_detail.html', {'object': video,
                                                       'favourite': favourite,
                                                       'to_watch': to_watch,
                                                       'like': like,
                                                       'dislike': dislike,
                                                       'total_likes': video.total_likes(),
                                                       'total_dislikes': video.total_dislikes()})


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


def favourite_view(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if video.favourite.filter(pk=request.user.id).exists():
        video.favourite.remove(request.user)
    else:
        video.favourite.add(request.user)
    return HttpResponseRedirect(video.get_absolute_url())


def favourite_list_view(request):
    favourites = request.user.favourite.all()
    return render(request, 'video/favourite.html', {'favourites': favourites})


def to_watch_view(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if video.to_watch.filter(pk=request.user.id).exists():
        video.to_watch.remove(request.user)
    else:
        video.to_watch.add(request.user)
    return HttpResponseRedirect(video.get_absolute_url())


def to_watch_list_view(request):
    to_watch = request.user.to_watch.all()
    return render(request, 'video/to_watch.html', {'to_watch': to_watch})


@login_required
def like_video(request):
    video = get_object_or_404(Video, pk=request.POST.get('video_pk'))
    if video.likes.filter(pk=request.user.pk).exists():
        video.likes.remove(request.user)
    else:
        video.likes.add(request.user)
        if video.dislikes.filter(pk=request.user.pk).exists():
            video.dislikes.remove(request.user)

    return HttpResponseRedirect(video.get_absolute_url())


@login_required
def dislike_video(request):
    video = get_object_or_404(Video, pk=request.POST.get('video_pk'))
    if video.dislikes.filter(pk=request.user.pk).exists():
        video.dislikes.remove(request.user)
    else:
        video.dislikes.add(request.user)
        if video.likes.filter(pk=request.user.pk).exists():
            video.likes.remove(request.user)

    return HttpResponseRedirect(video.get_absolute_url())
