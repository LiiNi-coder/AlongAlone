from unittest.util import _MAX_LENGTH
from django.db import models

#세부지점에 대한 모델
class Spot(models.Model):
    #지점 이름
    name=models.CharField(max_length=20)#지점 이름

    #지점 사진
    #ImageField.height_field, ImageField.width_field로 이미지 사진을 제한가능
    picture=models.ImageField()

    #지점 위치
    location=models.CharField()

    #date=models.DateFiled() <- 시간이 필요한가?

    #태그 1,2,3
    tag1=models.CharField(max_length=10)
    tag2=models.CharField(max_length=10)
    star=models.FloatField(max_length=5)

#Spot을 상속받는 식당클래스
class Restaurant(Spot):
    pass#식당만의 특이필드가 필요?
    
    