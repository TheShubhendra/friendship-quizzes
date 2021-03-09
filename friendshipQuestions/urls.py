from django.urls import path
from . import views

urlpatterns = [
    path("", views.FriendshipQuestionList.as_view(), name="Friendship Questions"),
]
