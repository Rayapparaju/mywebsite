
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import logout_view
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="about"),
    path('contact/', views.contact, name='contact'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
 ]