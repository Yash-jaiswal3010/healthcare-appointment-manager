from django.urls import path
from .views import *

urlpatterns = [

    path(
        "",
        LoginView.as_view(),
        name="login-page",
    ),

    path(
        "register/",
        RegisterView.as_view(),
        name="register-page",
    ),

    path(
        "patient/dashboard/",
        PatientDashboardView.as_view(),
        name="patient-dashboard",
    ),

    path(
        "patient/book/",
        BookAppointmentView.as_view(),
        name="book-appointment",
    ),

    path(
        "patient/appointments/",
        PatientAppointmentsView.as_view(),
        name="patient-appointments",
    ),

    path(
        "doctor/dashboard/",
        DoctorDashboardView.as_view(),
        name="doctor-dashboard",
    ),

    path(
        "doctor/appointments/",
        DoctorAppointmentsView.as_view(),
        name="doctor-appointments",
    ),

    path(
    "patient/profile/",
    PatientProfilePageView.as_view(),
    name="patient-profile-page",
    ),

    path(
    "doctor/profile/",
    DoctorProfilePageView.as_view(),
    name="doctor-profile-page",
    ),

    path(
    "patient/create-profile/",
    CreatePatientProfileView.as_view(),
    name="create-profile",
),
]