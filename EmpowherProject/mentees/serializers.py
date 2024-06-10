from rest_framework import serializers
from accounts.models import CustomUser

class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'country', 'is_verified', 'role','is_blocked')  # Add or remove fields as needed

