from rest_framework import serializers
from .models import Question, Choice, Quiz

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("choice_id", "choice")


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ("question_id", "question", "choices")


class QuizSerializer(QuizSerializer.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
