from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    questions = Question.objects.all()
    for question in questions:
        question.choices = question.choice_set.all()
    context = {
        'questions': questions,
    }
    return render (request,'quiz.html', context)