from django.db import models

# Create your models here.

# --------------------------
# Board 모델(테이블)은 
# --------------------------
# 제목(subject),
# 내용(content) 그리고
# 작성일시(create_date)를 속성
# --------------------------
class Board(models.Model):
    name = models.CharField(max_length=200)
    no = models.CharField(max_length=200, default='0000')
    email = models.CharField(max_length=200, default='example@example.com')
    tel = models.CharField(max_length=200, default='000-0000-0000')
    birth = models.CharField(max_length=100, default='0000-00-00')
    