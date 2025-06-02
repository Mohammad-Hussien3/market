from django.urls import path
from .views import UpdatePassword

urlpatterns = [
    path('updatepassword/', UpdatePassword.as_view(), name="updatepassword"),
]
