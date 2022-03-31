from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"ID: {self.id} Question Text: {self.question_text}" 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"ID: {self.id} Choice Text: {self.choice_text}"
