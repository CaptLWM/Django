from django.db import models

#1대1 매핑 / DB정의
# Create your models here. ORM(Object Relational Mapping)
class Question(models.Model): #DB 테이블 생성
    question_text = models.CharField(max_length=200) #클래스 변수
    pub_date = models.DateTimeField('date published') #클래스 변수

    def  __str__(self): #메소드 정의
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #FK로 Question DB 참조 / 질문에 맞는 선택지 추가 가능 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


