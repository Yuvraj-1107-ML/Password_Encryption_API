from django.urls import path
from .views import EncryptPasswordView

urlpatterns = [
    path('encrypt/', EncryptPasswordView.as_view(), name='encrypt-password'),
]