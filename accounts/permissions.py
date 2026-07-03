from rest_framework.permissions import BasePermission
from .models import Role
from doctors.models import DoctorAvailability

class IsAdminRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == Role.ADMIN
        )


class IsDoctorRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == Role.DOCTOR
        )


class IsPatientRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == Role.PATIENT
        )
    
