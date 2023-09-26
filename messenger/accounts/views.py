from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, LoginUserForm, UserForm, ProfileForm
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect



class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'registration/signup.html'
    success_url = '/appchat'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'user': request.user})
