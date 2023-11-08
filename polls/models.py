from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
   

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
 
class Open_answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.TextField(null=True)
    def __str__(self):
        return self.user_answer
    
class User(models.Model):
    photo_1 = models.CharField(max_length=200,null=True)
    photo_2 = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200,null=True)
    phone_num=models.CharField(max_length=200,null=True)
    gender = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    earing = models.IntegerField(default=0)

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer=models.IntegerField(default=0)