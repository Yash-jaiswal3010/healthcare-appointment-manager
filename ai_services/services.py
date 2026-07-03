import google.generativeai as genai

from django.conf import settings


genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_symptom_summary(symptoms):

    prompt = f"""
    You are a medical assistant.

    Summarize the patient's symptoms in concise bullet points.

    Symptoms:
    {symptoms}

    Keep the summary short and suitable for a doctor.
    """

    response = model.generate_content(prompt)

    return response.text


def generate_patient_summary(doctor_notes):

    prompt = f"""
    You are a medical assistant.

    Convert the doctor's clinical notes into a simple explanation
    that a patient can easily understand.

    Doctor Notes:
    {doctor_notes}

    Keep the language friendly and avoid medical jargon.
    """

    response = model.generate_content(prompt)

    return response.text