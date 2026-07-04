from accounts.models import Role

from rest_framework.permissions import BasePermission

# by this a doctor can edit only their own availability
class IsAvailabilityOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return (
            request.user.is_authenticated
            and request.user.role == Role.DOCTOR
            and obj.doctor == request.user.doctor_profile
        )