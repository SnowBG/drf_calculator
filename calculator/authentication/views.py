from rest_framework import viewsets
from rest_framework import permissions

from calculator.authentication import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    """Endpoint to view user's data."""

    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
