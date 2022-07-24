from django.db import models
from alongapp.models import Spot as spotmodels

class Comment(models.Model):
    #댓글내용
    body=models.TextField()
    
    #댓글단 사람(계정ID? 닉네임? 으로 따짐)
    ##공사중!! 계정앱이 완성되고나서 따질수있음.
    #author=models.CharField(max_length)

    #댓글단 시간(자동으로 적은 시간으로 기록됨)
    date=models.DateTimeField(auto_now_add=True)

    #해당 댓글이 달린 Spot클래스
    #on_delete=CASCADE 옵션은 게시글(spot클래스)가 삭제되면 자동으로 해당 댓글클래스도 모두 자동삭제되게하는 욥션
    post=models.ForeignKey(spotmodels, on_delete=models.CASCADE)    

    def __str__(self):
        return self.body