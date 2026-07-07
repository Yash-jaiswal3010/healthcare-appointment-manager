from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
# meta tells about the extra essential info like if i don't want to give permission for becoming admin after registeration then i will not mention kit on meta, element inside meta will be considered onlyy
    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "password",
        ]
# extra_kwargs-->the API response should never include a password. DRF has a solution for that, and it's called extra_kwargs.
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }
# validated_data-> it takes api input from frontend
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# login serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, attrs):

        email = attrs["email"]
        password = attrs["password"]

        user = authenticate(
            username=email,
            password=password,
        )

        if user is None:
            raise serializers.ValidationError("Invalid email or password")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
        },
    }
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "email",
            "role",
        ]


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self):
        try:
            RefreshToken(self.token).blacklist()
        except Exception:
            raise serializers.ValidationError(
                "Invalid or expired refresh token."
            )