from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Doctor
from .serializers import (
    DoctorReadSerializer,
    DoctorWriteSerializer,
)
from accounts.permissions import IsAdminRole
from .models import DoctorAvailability
from .serializers import (
    AvailabilityReadSerializer,
    AvailabilityWriteSerializer,
)
from accounts.permissions import IsDoctorRole

class DoctorListCreateView(generics.ListCreateAPIView):

    queryset = Doctor.objects.filter(
        is_verified=True
    )

    def get_serializer_class(self):

        if self.request.method == "POST":
            return DoctorWriteSerializer

        return DoctorReadSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsAdminRole(),
            ]

        return []
    

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Doctor.objects.all()

    lookup_field = "id"

    def get_serializer_class(self):

        if self.request.method in ["PUT", "PATCH"]:
            return DoctorWriteSerializer

        return DoctorReadSerializer

    def get_permissions(self):

        if self.request.method in [
            "PUT",
            "PATCH",
            "DELETE",
        ]:
            return [
                IsAuthenticated(),
                IsAdminRole(),
            ]

        return []
    

class AvailabilityListCreateView(generics.ListCreateAPIView):

    queryset = DoctorAvailability.objects.all()

    def get_serializer_class(self):

        if self.request.method == "POST":
            return AvailabilityWriteSerializer

        return AvailabilityReadSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsDoctorRole(),
            ]

        return []

    def perform_create(self, serializer):

        serializer.save(
            doctor=self.request.user.doctor_profile
        )
        

class AvailabilityDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = DoctorAvailability.objects.all()

    lookup_field = "id"

    def get_serializer_class(self):

        if self.request.method in [
            "PUT",
            "PATCH",
        ]:
            return AvailabilityWriteSerializer

        return AvailabilityReadSerializer

    def get_permissions(self):

        if self.request.method in [
            "PUT",
            "PATCH",
            "DELETE",
        ]:
            return [
                IsAuthenticated(),
                IsAvailabilityOwner(),
            ]

        return []