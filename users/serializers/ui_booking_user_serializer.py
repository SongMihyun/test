from rest_framework import serializers

from users.models import User


class BookingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "phone_number"]
