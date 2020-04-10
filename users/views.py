from django.shortcuts import render, redirect
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import (
    RegisterForm,
    UserEditForm,
    ProfileEditForm,
    ChangePasswordForm,
)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, 'Konto zostało utworzone')
            return redirect('users:login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_edit_form = UserEditForm(request.POST, instance=request.user)
        profile_edit_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            success(request, 'Dane zostały zapisane pomyślnie')
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_edit_form': user_edit_form,
                                                  'profile_edit_form': profile_edit_form})


@login_required
def change_password(request):
    """Widok zmiany hasła użytkownika.
    Oparta na: https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html"""
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            update_session_auth_hash(request, form.save())
            success(request, 'Hasło zostało zmienione')
            return redirect('users:profile')
        else:
            error(request, 'Nieprawidłowe dane')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})
