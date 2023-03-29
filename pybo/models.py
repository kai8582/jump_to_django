from django.db import models
from django.contrib.auth.models import User

#makemigrations, migrate이 필요한 경우는 모델의 속성이 변경되었을때뿐이다

# Create your models here.
class Question(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE, null=True,related_name='author_question')
    subject = models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True,blank=True)
    voter=models.ManyToManyField(User,related_name='voter_question')
    
    def __str__(self):
        return self.subject   #manage.py shell에서 id값 대신 제목을 표시할수있다

class Answer(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="author_answer")
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True,blank=True)
    voter=models.ManyToManyField(User,related_name="voter_answer")
    
    
class test(models.Model):
    subject=models.CharField(max_length=100)
    test_date=models.DateTimeField()
    