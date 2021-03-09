from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics


class FrienshipQuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
