from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogModelForm

def honbab(request):
    #블로그 글들을 모조리 띄우는 코드
    #데이터베이스로부터 views.py로 블로그 객체를 다 가져온 후에, render의 세번째 인자로 html에 넘김

    #posts = Blog.objects.all() #블로그 객체를 모두 가져오는 코드
    posts =Blog.objects.filter().order_by('-date')   #필터링해서 가져오기 날짜 오름차순(date) 내림차순(-date)
    return render(request, 'honbab.html', {'posts' : posts})

# django modelform을 이용해서 입력값을 받는 함수
def modelformcreate(request):
    #새 글 생성하기를 누르면 데이터베이스로 넘기기
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('honbab')
    #새 글을 입력받는 form을 띄워주기
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form' : form}) 

def detail(request, blog_id):
    #1. blog_id번째 블로그 글을 데이터베이스로부터 갖고와서
    #pk값을 이용해 특정 모델 객체 하나만 갖고 오기.#객체를 갖고오던지 없으면 404를 띄워라. 
    #pk가 blog_id인 블로그 객체를 가져옴.
    blog_detail = get_object_or_404(Blog, pk=blog_id)   
    #2. blog_id번째 블로그 글을 detail.html로 띄워주는 코드
    return render(request, 'detail.html', {'blog_detail' : blog_detail})

    

