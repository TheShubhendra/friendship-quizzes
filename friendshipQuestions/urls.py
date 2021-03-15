from django.urls import path
from . import views

urlpatterns = [
    path("questions/", views.FriendshipQuestionList.as_view(), name="Friendship Questions"),
    path("quiz/", views.FriendshipQuiz.as_view(), name="Friendship Quiz"),
]
