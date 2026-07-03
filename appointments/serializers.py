from datetime import date

from rest_framework import serializers

from .models import Appointment, AppointmentStatus
from doctors.models import DoctorAvailability
from patients.models import Patient


class AppointmentReadSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source="patient.user.full_name",
        read_only=True
    )

    doctor_name = serializers.SerializerMethodField()
    def get_doctor_name(self, obj):
        return f"Dr. {obj.doctor.user.full_name}"

    specialization = serializers.CharField(
        source="doctor.specialization.name",
        read_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "patient_name",
            "doctor_name",
            "specialization",
            "appointment_date",
            "appointment_time",
            "status",
            "symptoms",
            "symptom_summary",
            "doctor_notes",
            "patient_summary",
        ]


class AppointmentWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = [
            "doctor",
            "appointment_date",
            "appointment_time",
            "symptoms",
        ]

    def validate_appointment_date(self, value):

        if value < date.today():
            raise serializers.ValidationError(
                "Appointment date cannot be in the past."
            )

        return value

    def validate(self, attrs):

        doctor = attrs["doctor"]
        appointment_date = attrs["appointment_date"]
        appointment_time = attrs["appointment_time"]

        # Convert date to weekday
        weekday = appointment_date.strftime("%A").upper()

        # Check doctor availability
        available = DoctorAvailability.objects.filter(
            doctor=doctor,
            day=weekday,
            start_time__lte=appointment_time,
            end_time__gt=appointment_time,
        ).exists()

        if not available:
            raise serializers.ValidationError(
                "Doctor is not available at this time."
            )

        # Prevent double booking
        if Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            status__in=[
                AppointmentStatus.PENDING,
                AppointmentStatus.CONFIRMED,
            ]
        ).exists():

            raise serializers.ValidationError(
                "Doctor already has an appointment at this time."
            )

        return attrs
    
class DoctorAppointmentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = [
            "status",
            "doctor_notes",
        ]

    def validate_status(self, value):

        current_status = self.instance.status

        # No status change -> allow it
        if value == current_status:
            return value

        allowed_transitions = {
            AppointmentStatus.PENDING: [
                AppointmentStatus.CONFIRMED,
                AppointmentStatus.CANCELLED,
            ],
            AppointmentStatus.CONFIRMED: [
                AppointmentStatus.COMPLETED,
                AppointmentStatus.CANCELLED,
            ],
            AppointmentStatus.COMPLETED: [],
            AppointmentStatus.CANCELLED: [],
        }

        if value not in allowed_transitions[current_status]:
            raise serializers.ValidationError(
                f"Cannot change status from "
                f"{current_status} to {value}."
            )

        return value