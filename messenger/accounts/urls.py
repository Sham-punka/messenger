from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('profile/', edit_user, name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', RegisterUser.as_view(), name='register'),
]