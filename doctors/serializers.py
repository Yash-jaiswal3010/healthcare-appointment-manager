from rest_framework import serializers
from accounts.models import Role
from .models import (
    Specialization,
    Doctor,
    DoctorAvailability,
)

class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = "__all__"

class DoctorReadSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(
        source="user.full_name",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    specialization = serializers.CharField(
        source="specialization.name",
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = [
            "id",
            "doctor_name",
            "email",
            "specialization",
            "qualification",
            "experience",
            "consultation_fee",
            "hospital_name",
            "bio",
            "is_verified",
        ]


class DoctorWriteSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Doctor
        fields = [
            "user",
            "specialization",
            "qualification",
            "experience",
            "consultation_fee",
            "hospital_name",
            "bio",
            "is_verified",
        ]

        read_only_fields = [
            "is_verified",
        ]
    def validate_user(self, user):
        if user.role != Role.DOCTOR:
            raise serializers.ValidationError(
                "Selected user is not a doctor."
            )

        return user
    

class AvailabilityReadSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(
        source="doctor.user.full_name",
        read_only=True
    )

    class Meta:
        model = DoctorAvailability
        fields = [
            "id",
            "doctor_name",
            "day",
            "start_time",
            "end_time",
        ]

    
class AvailabilityWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorAvailability
        fields = [
            "day",
            "start_time",
            "end_time",
        ]

    def validate(self, attrs):

        doctor = attrs["doctor"]
        day = attrs["day"]
        start_time = attrs["start_time"]
        end_time = attrs["end_time"]

        overlapping_slots = DoctorAvailability.objects.filter(
            doctor=doctor,
            day=day,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        if self.instance:
            overlapping_slots = overlapping_slots.exclude(
                pk=self.instance.pk
            )

        if overlapping_slots.exists():
            raise serializers.ValidationError(
                "This availability slot overlaps with an existing slot."
            )

        return attrs