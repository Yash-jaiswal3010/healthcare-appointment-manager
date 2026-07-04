from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "login.html"


class RegisterView(TemplateView):
    template_name = "register.html"


class PatientDashboardView(TemplateView):
    template_name = "patient/dashboard.html"


class BookAppointmentView(TemplateView):
    template_name = "patient/book_appointment.html"


class PatientAppointmentsView(TemplateView):
    template_name = "patient/appointments.html"


class DoctorDashboardView(TemplateView):
    template_name = "doctor/dashboard.html"


class DoctorAppointmentsView(TemplateView):
    template_name = "doctor/appointments.html"


class PatientProfilePageView(TemplateView):
    template_name = "patient/profile.html"


class DoctorProfilePageView(TemplateView):
    template_name = "doctor/profile.html"

class CreatePatientProfileView(TemplateView):
    template_name="patient/create_profile.html"