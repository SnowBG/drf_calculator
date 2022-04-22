"""Serializers for operations management."""
from rest_framework import serializers

from calculator.operations import models


class OperationHistorySerializer(serializers.ModelSerializer):
    model = serializers.OperationHistory

    class Meta:
        fields = ['user', 'values', 'operation_type', 'result', 'created_at']
        extra_kwargs = {
            'email': {'read_only': True},
        }
