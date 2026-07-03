from django.db import models
from accounts.models import User
from django.core.exceptions import ValidationError

class Specialization(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.PROTECT,
        related_name="doctors"
    )

    qualification = models.TextField()

    experience = models.PositiveIntegerField()

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    hospital_name = models.CharField(max_length=200)

    bio = models.TextField(blank=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.user.full_name}"
    
# this will help in appointment 
class WeekDay(models.TextChoices):
    MONDAY = "MONDAY", "Monday"
    TUESDAY = "TUESDAY", "Tuesday"
    WEDNESDAY = "WEDNESDAY", "Wednesday"
    THURSDAY = "THURSDAY", "Thursday"
    FRIDAY = "FRIDAY", "Friday"
    SATURDAY = "SATURDAY", "Saturday"
    SUNDAY = "SUNDAY", "Sunday"


class DoctorAvailability(models.Model):

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="availability_slots"
    )

    day = models.CharField(
        max_length=20,
        choices=WeekDay.choices
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError(
                "Start time must be earlier than end time."
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "doctor",
                    "day",
                    "start_time",
                    "end_time",
                ],
                name="unique_doctor_slot"
            )
        ]

    def __str__(self):
        return (
            f"{self.doctor.user.full_name} | "
            f"{self.day} | "
            f"{self.start_time} - {self.end_time}"
        )