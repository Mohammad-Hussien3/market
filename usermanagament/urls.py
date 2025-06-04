from django.urls import path
from .views import UpdatePassword, LogIn

urlpatterns = [
    path('updatepassword/', UpdatePassword.as_view(), name="updatepassword"),
    path('login/', LogIn.as_view(), name='login'),
]
