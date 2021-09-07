from django.urls import path
from .views import UserRegistrationView,ApiTestView

urlpatterns = [
    path("api/register/",UserRegistrationView.as_view(),name='register'),
    path("api/test/",ApiTestView.as_view(),name="test"),
]
