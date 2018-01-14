from django.db import models


class Question(models.Model):
    author = models.CharField(max_length=50)
    question_title = models.CharField(max_length=100)
    question_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.author} - {self.pub_date}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    answer_text = models.TextField()
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.author} - {self.pub_date}'
