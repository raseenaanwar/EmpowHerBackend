from rest_framework import serializers
from accounts.models import CustomUser

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'country', 'is_verified', 'role','is_blocked')  # Add or remove fields as needed

class UserGeneralProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profession', 'country', 'timezone', 'language', 'profile_image']
