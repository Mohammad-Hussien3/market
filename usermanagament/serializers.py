from rest_framework import serializers
from .models import Profile, Admin


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('referral_link', 'referred_by', )


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'