#  Healthcare Appointment Manager

A full-stack Healthcare Appointment Management System built using **Django**, **Django REST Framework**, **PostgreSQL**, **JWT Authentication**, and **Google Gemini AI**.

The application allows patients to book appointments, doctors to manage appointments, and uses AI to automatically summarize patient symptoms.

---

#  Features

## Authentication

- JWT Authentication
- Secure Login & Logout
- Role-Based Access Control
- Patient
- Doctor
- Admin

---

## Patient Features

- Register & Login
- Book Appointment
- View Appointment History
- View Doctor Profiles
- View/Edit Patient Profile
- AI Generated Symptom Summary

---

## Doctor Features

- Login
- View Appointments
- Update Appointment Status
- Add Doctor Notes
- View Doctor Profile

---

## AI Features

Google Gemini is used to automatically summarize patient symptoms after appointment booking.

Example:

Input:

```
Patient has severe headache, fever, nausea and body pain for three days.
```

Output:

```
Headache
Fever
Nausea
Body Pain
```

---

#  Tech Stack

Backend

- Django
- Django REST Framework

Database

- PostgreSQL

Authentication

- JWT (SimpleJWT)

AI

- Google Gemini API

Frontend

- HTML
- CSS
- JavaScript

Deployment

- Render
- Neon PostgreSQL

---

#  Project Structure

```
Healthcare Appointment Manager
│
├── accounts
├── appointments
├── doctors
├── patients
├── notifications
├── ai_services
├── frontend
├── static
├── templates
├── config
├── requirements.txt
├── build.sh
└── manage.py
```

---

#  Setup Guide

## Clone Repository

```bash
git clone https://github.com/Yash-jaiswal3010/healthcare-appointment-manager.git

cd healthcare-appointment-manager
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create

```
.env
```

using the sample below.

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

---

#  .env.example

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_database_url

GEMINI_API_KEY=your_gemini_api_key

EMAIL_HOST=smtp.gmail.com

EMAIL_PORT=587

EMAIL_HOST_USER=your_email@gmail.com

EMAIL_HOST_PASSWORD=your_app_password

EMAIL_USE_TLS=True
```

---

# 📚 API Documentation

## Authentication

| Method | Endpoint |
|----------|---------------------------|
| POST | /api/auth/register/ |
| POST | /api/auth/login/ |
| POST | /api/auth/logout/ |

---

## Doctors

| Method | Endpoint |
|----------|---------------------------|
| GET | /api/doctors/ |
| GET | /api/doctors/<id>/ |
| GET | /api/doctors/profile/ |
| GET | /api/doctors/appointments/ |

---

## Patients

| Method | Endpoint |
|----------|---------------------------|
| GET | /api/patients/profile/ |
| PATCH | /api/patients/profile/ |

---

## Appointments

| Method | Endpoint |
|----------|---------------------------|
| GET | /api/appointments/ |
| POST | /api/appointments/ |
| PATCH | /api/appointments/<id>/ |

---

#  Database Schema

## User

- id
- full_name
- email
- password
- role

---

## Patient

- id
- user
- date_of_birth
- gender
- blood_group
- phone_number
- address
- emergency_contact

---

## Doctor

- id
- user
- specialization
- qualification
- experience
- consultation_fee
- hospital_name
- bio

---

## Appointment

- id
- patient
- doctor
- appointment_date
- appointment_time
- status
- symptoms
- symptom_summary
- doctor_notes
- patient_summary

---

#  LLM Prompt

Prompt used for Google Gemini

```
Summarize the following patient symptoms into concise medical points.

Symptoms:
{patient_symptoms}
```

---

#  Hosted Application

Application URL

```
https://your-render-url.onrender.com
```

---

#  Author

**Yash Jaiswal**

GitHub

https://github.com/Yash-jaiswal3010
