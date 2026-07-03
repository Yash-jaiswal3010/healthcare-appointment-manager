from django.urls import path

from .views import (
    AppointmentListCreateView,
    DoctorAppointmentListView,
    DoctorAppointmentUpdateView,
)

urlpatterns = [

    path(
        "",
        AppointmentListCreateView.as_view(),
        name="appointment-list-create",
    ),

    path(
        "doctor/",
        DoctorAppointmentListView.as_view(),
        name="doctor-appointments",
    ),

    path(
        "doctor/<int:pk>/",
        DoctorAppointmentUpdateView.as_view(),
        name="doctor-appointment-update",
    ),
]