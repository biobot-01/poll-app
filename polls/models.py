from django.db import models


class Question(models.Model):
    """Question model."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Return question text."""
        return self.question_text


class Choice(models.Model):
    """Choice model."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return choice text."""
        return self.choice_text
