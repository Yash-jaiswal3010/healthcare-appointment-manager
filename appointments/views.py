from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.services import (
    send_appointment_booked_email,
    send_appointment_confirmed_email,
    send_appointment_cancelled_email,
    send_appointment_completed_email,
)

from ai_services.services import (
    generate_symptom_summary,
    generate_patient_summary,
)

from appointments.models import Appointment, AppointmentStatus
from .serializers import (
    AppointmentReadSerializer,
    AppointmentWriteSerializer,
    DoctorAppointmentUpdateSerializer,
)

from accounts.permissions import (
    IsPatientRole,
    IsDoctorRole,
)


class AppointmentListCreateView(
    generics.ListCreateAPIView
):

    permission_classes = [
        IsAuthenticated,
        IsPatientRole,
    ]

    def get_queryset(self):
        return Appointment.objects.filter(
            patient=self.request.user.patient_profile
        )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AppointmentWriteSerializer
        return AppointmentReadSerializer

    def create(self, request, *args, **kwargs):

        write_serializer = self.get_serializer(
            data=request.data
        )

        write_serializer.is_valid(
            raise_exception=True
        )

        appointment = write_serializer.save(
            patient=request.user.patient_profile
        )

        appointment.symptom_summary = generate_symptom_summary(
            appointment.symptoms
        )

        appointment.save(
            update_fields=["symptom_summary"]
        )

        read_serializer = AppointmentReadSerializer(
            appointment
        )
        # Send email notification
        send_appointment_booked_email(appointment)

        read_serializer = AppointmentReadSerializer(
        appointment
        )
        return Response(
            read_serializer.data,
            status=status.HTTP_201_CREATED,
        )


class DoctorAppointmentListView(
    generics.ListAPIView
):

    serializer_class = AppointmentReadSerializer

    permission_classes = [
        IsAuthenticated,
        IsDoctorRole,
    ]

    def get_queryset(self):

        return Appointment.objects.filter(
            doctor=self.request.user.doctor_profile
        ).order_by(
            "appointment_date",
            "appointment_time",
        )


class DoctorAppointmentUpdateView(
    generics.UpdateAPIView
):

    serializer_class = DoctorAppointmentUpdateSerializer

    permission_classes = [
        IsAuthenticated,
        IsDoctorRole,
    ]

    def get_queryset(self):

        return Appointment.objects.filter(
            doctor=self.request.user.doctor_profile
        )

    def update(self, request, *args, **kwargs):

        appointment = self.get_object()

        old_status = appointment.status
        old_notes = appointment.doctor_notes

        serializer = self.get_serializer(
            appointment,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True
        )

        appointment = serializer.save()
        if appointment.status == AppointmentStatus.CONFIRMED:
            send_appointment_confirmed_email(
        appointment
    )

        elif appointment.status == AppointmentStatus.CANCELLED:
            send_appointment_cancelled_email(
        appointment
    )

        should_generate_summary = (
            appointment.status == AppointmentStatus.COMPLETED
            and appointment.doctor_notes
            and (
                old_status != AppointmentStatus.COMPLETED
                or old_notes != appointment.doctor_notes
            )
        )

        if should_generate_summary:

            appointment.patient_summary = (
                generate_patient_summary(
                    appointment.doctor_notes
                )
            )

            appointment.save(
                update_fields=["patient_summary"]
            )
            send_appointment_completed_email(
            appointment
            )
        return Response(
            AppointmentReadSerializer(
                appointment
            ).data,
            status=status.HTTP_200_OK,
        )
    
    