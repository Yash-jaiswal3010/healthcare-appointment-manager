from django.urls import path

from .views import (
    PatientCreateView,
    PatientProfileView,
)

urlpatterns = [

    path(
        "",
        PatientCreateView.as_view(),
        name="patient-create",
    ),

    path(
        "profile/",
        PatientProfileView.as_view(),
        name="patient-profile",
    ),
]