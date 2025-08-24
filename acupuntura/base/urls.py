from django.urls import path
from acupuntura.base.views import base

app_name = "base"

urlpatterns = [
    path("", base, name="base")
    ]