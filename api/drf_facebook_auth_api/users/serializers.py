from rest_framework import serializers

from users.models import User


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "profile_image",
        )
        read_only_fields = ("username", "email", "is_staff", "is_active", "profile_image")
