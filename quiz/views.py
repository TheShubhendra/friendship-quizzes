from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics


class GetQuestions(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer