from django.urls import path
from .views import (
    DoctorListCreateView,
    DoctorDetailView,
    AvailabilityListCreateView,
    AvailabilityDetailView,
)

urlpatterns = [
    path(
        "",
        DoctorListCreateView.as_view(),
        name="doctor-list",
    ),

    path(
        "<int:id>/",
        DoctorDetailView.as_view(),
        name="doctor-detail",
    ),
    path(
        "availability/",
        AvailabilityListCreateView.as_view(),
        name="availability-list",
    ),

    path(
        "availability/<int:id>/",
        AvailabilityDetailView.as_view(),
        name="availability-detail",
    ),
]