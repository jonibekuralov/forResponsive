from django.urls import path

from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
from .views import user_login, dashboard_view, user_register, EditUserView, my_logout_view

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', my_logout_view, name="logout"),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('passport-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', dashboard_view, name="user_profile"),
    path('profile/edit', EditUserView.as_view(), name='edit_user'),
    path('signup/', user_register, name='user_register'),

]
