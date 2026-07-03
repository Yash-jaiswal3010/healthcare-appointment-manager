from django.conf import settings
from django.core.mail import send_mail


def send_appointment_email(
    appointment,
    subject,
    message,
):

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[
            appointment.patient.user.email
        ],
    )


def send_appointment_booked_email(
    appointment,
):

    message = f"""
Hello {appointment.patient.user.full_name},

Your appointment has been booked successfully.

Doctor:
Dr. {appointment.doctor.user.full_name}

Specialization:
{appointment.doctor.specialization.name}

Date:
{appointment.appointment_date}

Time:
{appointment.appointment_time}

Status:
{appointment.status}

Symptoms:
{appointment.symptoms}

AI Symptom Summary:
{appointment.symptom_summary}

Thank you.
"""

    send_appointment_email(
        appointment,
        "Appointment Booked Successfully",
        message,
    )


def send_appointment_confirmed_email(
    appointment,
):

    message = f"""
Hello {appointment.patient.user.full_name},

Good news!

Your appointment with
Dr. {appointment.doctor.user.full_name}
has been CONFIRMED.

Date:
{appointment.appointment_date}

Time:
{appointment.appointment_time}

See you soon.
"""

    send_appointment_email(
        appointment,
        "Appointment Confirmed",
        message,
    )


def send_appointment_cancelled_email(
    appointment,
):

    message = f"""
Hello {appointment.patient.user.full_name},

Unfortunately,

your appointment has been CANCELLED.

Please book another slot.

Thank you.
"""

    send_appointment_email(
        appointment,
        "Appointment Cancelled",
        message,
    )


def send_appointment_completed_email(
    appointment,
):

    message = f"""
Hello {appointment.patient.user.full_name},

Your appointment has been completed.

Doctor Notes

{appointment.doctor_notes}

AI Patient Summary

{appointment.patient_summary}

Wish you a speedy recovery.
"""

    send_appointment_email(
        appointment,
        "Appointment Completed",
        message,
    )