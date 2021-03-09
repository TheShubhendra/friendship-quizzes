from django.db import models


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    choice_id = models.AutoField(primary_key=True)
    choice = models.CharField(max_length=30)

    def __str__(self):
        return self.choice