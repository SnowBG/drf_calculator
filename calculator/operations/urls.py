from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from calculator.operations import views

app_name = 'operations'

router = SimpleRouter()

urlpatterns = [
    path(
        'operation/',
        views.OperationsInputSerializer,
        name='operation',
    ),
    path('', include(router.urls)),
]
