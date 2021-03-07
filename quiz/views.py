from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import generics
        

class GetQuestions(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class GetChoices(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
