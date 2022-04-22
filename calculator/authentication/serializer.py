"""Serializers for accounts management."""
from rest_framework import serializers

from calculator.authentication import models


class UserSerializer(serializers.ModelSerializer):
    """Serializes the user's datas."""

    class Meta:
        model = models.User
        fields = "__all__"
