from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
 path('', views.check_form, name='check'),
 path('login', views.login, name='login'),
 path('logout/', views.logout, name='logout'),
 path('register/', views.register, name='register'),
 path('doctor-register/', views.doctor_register, name='doctor-register'),
 path('forget-password/', views.forget_password, name='forget-password'),
  path('google/', views.google, name='google'),

# path('password_rest/',auth_views.PasswordResetView.as_view(), name='password_reset'),
# path('password_rest/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
# path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
# path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
