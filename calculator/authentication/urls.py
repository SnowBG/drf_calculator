from django.contrib import admin
from django.urls import path, include

from calculator.operations import views

urlpatterns = [
    path('', admin.site.urls),
]
