"""App URLs"""

# Django
from django.urls import path

# AA Example App
from example import views

app_name: str = "example"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.index, name="index"),
]
