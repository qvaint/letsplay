from django.db import models

# Create your models here
class Question(models.Model):
  platform_choice = models.CharField(max_length=200)
  platform_name = models.CharField(max_length=200)
  game_preference = models.CharField(max_length=200)
  def __str__(self):
    return self.question_text

class Result(models.Model):
  question = models.ForeignKey(Question)
  def __str__(self):
    return self.result_text

    