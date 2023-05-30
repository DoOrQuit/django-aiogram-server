from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "password",
            "email",
            "created_at",
            "updated_at"
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
