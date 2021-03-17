import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(_('Publication date'))

    def __str__(self):
        return "{}: {}".format(self.id, self.question_text)

    def __repr__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() \
            - datetime.timedelta(days=1)
    was_published_recently.short_description = 'Опубликовано недавно'

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{}: {} ({})".format(
            self.question, self.choice_text,
            self.id
        )

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")
