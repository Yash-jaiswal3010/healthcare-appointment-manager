from rest_framework import serializers
from .models import Patient

class PatientReadSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source="user.full_name",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = Patient
        fields = [
            "id",
            "patient_name",
            "email",
            "date_of_birth",
            "gender",
            "blood_group",
            "phone_number",
            "address",
            "emergency_contact",
        ]


class PatientWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            "date_of_birth",
            "gender",
            "blood_group",
            "phone_number",
            "address",
            "emergency_contact",
        ]

    def validate(self, attrs):

        if (
            self.instance is None
            and Patient.objects.filter(
            user=self.context["request"].user
                ).exists()
            ):
            raise serializers.ValidationError(
            "Patient profile already exists."
        )

        return attrs