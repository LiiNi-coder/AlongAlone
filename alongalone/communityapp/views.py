from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogModelForm

# index, honcafe, honnol, honsul은 각 게시판 메인화면 html을 보여주는 함수
def index(request):
    #posts = Blog.objects.all() #블로그 객체를 모두 가져오는 코드
    posts =Blog.objects.filter().order_by('-date')   #필터링해서 가져오기 날짜 오름차순(date) 내림차순(-date)
    return render(request, 'index.html', {'posts' : posts})

def honcafe(request):
    posts =Blog.objects.filter().order_by('-date')   
    return render(request, 'honcafe.html', {'posts' : posts})

def honnol(request):
    posts =Blog.objects.filter().order_by('-date')
    return render(request, 'honnol.html', {'posts' : posts})

def honsul(request):
    posts =Blog.objects.filter().order_by('-date')  
    return render(request, 'honsul.html', {'posts' : posts})



# django modelform을 이용해서 입력값을 받는 함수(새 글 생성하기 눌렀을 때 함수)
def honbabwrite(request):
    #새 글 생성하기를 누르면 데이터베이스로 넘기기
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('index')
    #새 글을 입력받는 form을 띄워주기
    else:
        form = BlogModelForm()
    return render(request, 'honbabwrite.html', {'form' : form}) 

def honsulwrite(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('honsul')
    else:
        form = BlogModelForm()
    return render(request, 'honsulwrite.html', {'form' : form}) 

def honnolwrite(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('honnol')
    else:
        form = BlogModelForm()
    return render(request, 'honnolwrite.html', {'form' : form}) 

def honcafewrite(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('honcafe')
    else:
        form = BlogModelForm()
    return render(request, 'honcafewrite.html', {'form' : form}) 


def detail(request, blog_id):
    #1. blog_id번째 블로그 글을 데이터베이스로부터 갖고와서
    #pk값을 이용해 특정 모델 객체 하나만 갖고 오기.#객체를 갖고오던지 없으면 404를 띄워라. 
    #pk가 blog_id인 블로그 객체를 가져옴.
    blog_detail = get_object_or_404(Blog, pk=blog_id)   
    #2. blog_id번째 블로그 글을 detail.html로 띄워주는 코드
    return render(request, 'detail.html', {'blog_detail' : blog_detail})

def honbabdetail(request):
    return render(request, 'honbabdetail.html')

def honcafedetail(request):
    return render(request, 'honcafedetail.html')

def honsuldetail(request):
    return render(request, 'honsuldetail.html')

def honnoldetail(request):
    return render(request, 'honnoldetail.html')

