from django.shortcuts import render
from .models import Question, Quiz
from .serializers import (
    QuestionSerializer,
    QuizSerializer,
    )
from rest_framework import generics
from rest_framework.views import APIView

class FriendshipQuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get']


class FriendshipQuiz(APIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
