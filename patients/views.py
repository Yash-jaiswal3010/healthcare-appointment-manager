from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Patient
from .serializers import (
    PatientReadSerializer,
    PatientWriteSerializer,
)

from accounts.permissions import IsPatientRole

class PatientProfileView(
    generics.RetrieveUpdateAPIView
):

    permission_classes = [
        IsAuthenticated,
        IsPatientRole,
    ]
    def get_object(self):
        
         return get_object_or_404(
            Patient,
            user=self.request.user
        )

    def get_serializer_class(self):

        if self.request.method in ["PUT", "PATCH"]:
            return PatientWriteSerializer

        return PatientReadSerializer


class PatientCreateView(
    generics.CreateAPIView
):

    serializer_class = PatientWriteSerializer

    permission_classes = [
        IsAuthenticated,
        IsPatientRole,
    ]

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )