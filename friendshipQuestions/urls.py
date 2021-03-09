from django.urls import path
from . import views

urlpatterns = [
    path("questions/", views.FriendshipQuestionList.as_view(), name="Friendship Questions"),
]
