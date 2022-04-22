from rest_framework import viewsets
from rest_framework import permissions

from calculator.operations import serializers, models


class OperationHistoryViewSet(viewsets.ModelViewSet):
    """Endpoint to view operations's data."""

    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
