from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class AppointmentStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    CONFIRMED = "CONFIRMED", "Confirmed"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"


class Appointment(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.PENDING
    )

    symptoms = models.TextField()
    symptom_summary = models.TextField(
    blank=True
    )

    doctor_notes = models.TextField(
        blank=True
    )

    patient_summary = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["appointment_date", "appointment_time"]

    def __str__(self):
        return (
            f"{self.patient.user.full_name} -> "
            f"Dr. {self.doctor.user.full_name} "
            f"({self.appointment_date} {self.appointment_time})"
        )