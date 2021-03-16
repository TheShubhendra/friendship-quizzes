from rest_framework import serializers
from .models import (
    Question,
    Choice,
    Quiz,
    Response,
    )

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("choice_id", "choice")


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ("question_id", "question", "choices")


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("quiz_id", "name", "data")


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ("response_id", "name", "score")
