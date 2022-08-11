from django.db import models

# class 새로 만들거나 변경할 때마다 데이터베이스에 반영해줘야 함.
# makemigrations -> migrate 잊지 말기
class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, default ="") #어떤 게시판에 글을 쓸 것인지 카테고리 선택(툴바 선택 미구현)
    photo = models.ImageField(blank=True, null=True, upload_to ='blog_photo')   
    #미디어 파일을 업로드 할 때마다 자동으로 'blog_photo'라는 폴더 생성해서 그 안에 파일들
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  #현재 시간을 자동으로 추가.

    def __str__(self):
        return self.title
###장고는 우리가 primary key 지정안하면 id라는 키를 자동으로 만듬.