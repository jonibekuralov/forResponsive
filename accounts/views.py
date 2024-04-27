from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import View

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])

            if user is not None:
                login(request, user)
                return redirect('home_list')
            else:
                messages.error(request, 'Username yoki Parol xato!')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def my_logout_view(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)

        return redirect('home_list')

    # Agar POST yoki GET bo'lmasa, `405 Method Not Allowed` qaytariladi
    return render(request, "app/logged_out.html", {})


def dashboard_view(request):
    if request.user.is_anonymous:
        return redirect(reverse('login'))
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Обработка ситуации, когда профиль не существует
        profile = None
    context = {
        'user': user,
        'profile': profile,

    }
    return render(request, 'pages/user_profile.html', context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form})


class SignUpView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
        if user_form is not None:
            return HttpResponse(render(request, 'news/404.html'))


class EditUserView(LoginRequiredMixin, View):

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'account/profile_edit.html', context)

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile')
        else:
            # В случае ошибок, возвращаем формы с сообщениями об ошибках
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(request, 'account/profile_edit.html', context)
