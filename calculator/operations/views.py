from rest_framework import viewsets
from rest_framework import permissions

from calculator.operations import serializers, models, operations
from calculator.operations.serializers import (
    OperationsInputSerializer,
    OperationsOutSerializer,
)


class OperationView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        op_data = OperationsInputSerializer(data=request.data)

        if not op_data.is_valid():
            raise Exception

        value_a = op_data.data.value_a
        value_b = op_data.data.value_b
        operation = op_data.data.operation
        user_id = self.request.user.id

        if operation == 'addition':
            result = operations.Operations.addition(value_a, value_b)
        elif operation == 'subtraction':
            result = operations.Operations.subtraction(value_a, value_b)
        elif operation == 'division':
            result = operations.Operations.division(value_a, value_b)
        elif operation == 'multiply':
            result = operations.Operations.multiply(value_a, value_b)
        else:
            raise Exception
        models.OperationHistory.objects.create(
            user=user_id,
            value_a=value_a,
            value_b=value_b,
            operation_type=operation,
            result=result,
        )
        return OperationsOutSerializer(
            value_a=value_a,
            value_b=value_b,
            operation=operation,
            result=result,
        )


class OperationHistoryViewSet(viewsets.ModelViewSet):
    """Endpoint to view operations's data."""

    queryset = models.Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
