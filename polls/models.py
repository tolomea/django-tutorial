import datetime

from django.db import models
from django.utils import timezone


class LibQuerySet(models.QuerySet):
    pass


LibManager = models.Manager.from_queryset(LibQuerySet)


class LibModel(models.Model):
    class Meta:
        abstract = True
        base_manager_name = "lib_manager"

    lib_manager = LibManager()
    objects = LibManager()


class QuestionManager(LibManager):
    pass


class Question(LibModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    objects = QuestionManager()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(LibModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
