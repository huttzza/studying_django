from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200) #제목 : 200자까지 입력, 글자 수 제한 시에는 CharField 함수
    content = models.TextField() #내용 : 글자 수 제한 없는 데이터는 TextField 함수
    create_date = models.DateTimeField()

    def __str__(self): #사람이 보기 쉽게
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #어떤 모델이 다른 모델을 속성으로 가질 때 ForeignKey 함수
    #on_delete : 질문 삭제되면 답변도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()