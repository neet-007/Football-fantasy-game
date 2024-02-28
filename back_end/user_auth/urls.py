from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('get-csrftoken', views.GetCSRFToken.as_view(), name='get-csrftoken'),
    path('check-user', views.CheckUserView.as_view(), name='check-user'),
]