from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetQuestions.as_view(), name="questions"),
]
