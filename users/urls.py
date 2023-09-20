from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UsersCreateView, UsersUpdateView, UsersDeleteView, VerificationView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UsersCreateView.as_view(), name='register'),
    path('profile/', UsersUpdateView.as_view(), name='profile'),
    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='delete_user'),
    path('verification/<int:pk>/', VerificationView.as_view(), name='verification'),
]
