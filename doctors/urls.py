from django.urls import path
from .views import (
    DoctorProfileView,
    DoctorListCreateView,
    DoctorDetailView,
    AvailabilityListCreateView,
    AvailabilityDetailView,
)

urlpatterns = [

    path(
        "profile/",
        DoctorProfileView.as_view(),
        name="doctor-profile",
    ),

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