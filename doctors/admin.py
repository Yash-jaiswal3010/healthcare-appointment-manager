from django.contrib import admin
from .models import (
    Specialization,
    Doctor,
    DoctorAvailability,
)

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "specialization",
        "experience",
        "consultation_fee",
        "is_verified",
    )

    list_filter = (
        "specialization",
        "is_verified",
    )

    search_fields = (
        "user__full_name",
        "user__email",
    )


@admin.register(DoctorAvailability)
class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        "doctor",
        "day",
        "start_time",
        "end_time",
    )

    list_filter = ("day",)

    search_fields = (
        "doctor__user__full_name",
    )