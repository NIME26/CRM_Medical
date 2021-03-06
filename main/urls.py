from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', views.home, name='admin'),
    path('', views.home, name='home'),
    path('doctor_detail/<int:pk>/', views.doctor, name='doctor_detail'),
    path('patient/', views.patient, name='patient'),
    path('service/', views.service, name='service'),
    path('staff/', views.staff, name='staff'),
    path('appointment/', views.appointment, name='appointment'),
    path('create_appointment/', views.create_appointment,
         name='create_appointment'),
    path('updateAppointment/<int:pk>/',
         views.updateAppointment, name='updateAppointment'),
    path('deleteAppointment/<int:pk>/',
         views.deleteAppointment, name='deleteAppointment'),
    path('patients/', views.patient, name='patients'),
    path('update_home/<int:pk>/', views.update_home, name='update_home'),
    path('delete_home/<int:pk>/', views.delete_home, name='delete_home'),
    path('create_service_home', views.create_service_home,
         name='create_service_home'),
    path('create_service', views.create_service,
         name='create_service'),
    path('update_service/<int:pk>/', views.update_service, name='update_service'),
    path('delete_service/<int:pk>/', views.delete_service, name='delete_service'),
    path('create_doctor', views.create_doctor, name='create_doctor'),
    path('update_doctor/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('update_patient/<int:pk>/', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
