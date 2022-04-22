"""Models to implement the operations records."""
from django.db import models
from calculator.operations.operations import Operations
from calculator.authentication.models import Profile


class OperationType:
    """Defines the type of operation to be done."""

    ADD = 'addition'
    SUB = 'subtraction'
    DIV = 'division'
    MUL = 'multiplication'

    CHOICE = (
        (ADD, 'adição'),
        (SUB, 'subtração'),
        (DIV, 'divisão'),
        (MUL, 'multiplicação'),
    )


class OperationHistory(models.Model):
    """Record operations in the database."""

    user = models.OneToOneField(
        Profile, verbose_name="Usuário", on_delete=models.PROTECT
    )
    values = models.JSONField(
        verbose_name='valores', help_text="Valores para efetuar a operação."
    )
    operation_type = models.CharField(
        verbose_name='Tipo de operação',
        default=OperationType.ADD,
        null=False,
        choices=OperationType.CHOICE,
        max_length=20,
    )
    result = models.IntegerField(verbose_name='resultado')
    created_at = models.DateTimeField(
        verbose_name='criado em', editable=False, auto_now_add=True
    )
