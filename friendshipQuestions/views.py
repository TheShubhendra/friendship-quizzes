from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics


class FriendshipQuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get']
