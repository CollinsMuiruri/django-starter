from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='shule_users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='shule_users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='shule_users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='shule_users/password_reset_complete.html'), name='password_reset_complete'),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='shule_users/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='shule_users/password_change_done.html'), name='password_change_done'),
]