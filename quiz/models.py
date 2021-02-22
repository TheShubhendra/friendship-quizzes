from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_value = models.CharField(max_length=200)
    choice_image = models.CharField(max_length=200, default=None, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_value
