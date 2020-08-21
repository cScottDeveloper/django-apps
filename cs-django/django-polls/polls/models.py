from django.db import models

# Create your models here.
# Any changes made to the models.py file must be migrated
# Use command: python manage.py makemigrations polls acts as staging
# to set the choices
# Use command: python manage.py migrate
class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text