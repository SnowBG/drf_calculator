"""Serializers for operations management."""
from rest_framework import serializers

from calculator.operations import models


class OperationsInputSerializer(serializers.Serializer):
    value_a = serializers.IntegerField()
    value_b = serializers.IntegerField()
    operation = serializers.CharField()


class OperationsOutSerializer(OperationsInputSerializer):
    result = serializers.IntegerField()


class OperationHistorySerializer(serializers.ModelSerializer):
    model = models.OperationHistory

    class Meta:
        fields = ['user', 'values', 'operation_type', 'result', 'created_at']
        extra_kwargs = {
            'email': {'read_only': True},
        }
