from django.urls import path, include
from .views import Profile
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', views.registration, name = "registration"),
    path('profile/', Profile.as_view(), name='profile'),
]