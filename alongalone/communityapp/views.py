from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogModelForm

#게시판 메인 화면 관련 함수
def index(request):
    #posts = Blog.objects.all() #블로그 객체를 모두 가져오는 코드
    posts =Blog.objects.filter().order_by('-date')   #필터링해서 가져오기 날짜 오름차순(date) 내림차순(-date)
    return render(request, 'index.html', {'posts' : posts}) #잠깐만 index로 말고 board_main으로 보내보자(다시)

def honcafe(request):
    posts =Blog.objects.filter().order_by('-date')   
    return render(request, 'honcafe.html', {'posts' : posts})

def honnol(request):
    posts =Blog.objects.filter().order_by('-date')
    return render(request, 'honnol.html', {'posts' : posts})

def honsul(request):
    posts =Blog.objects.filter().order_by('-date')  
    return render(request, 'honsul.html', {'posts' : posts})

#글쓰기 화면 함수
# django modelform을 이용해서 입력값을 받는 함수(새 글 생성하기 눌렀을 때 함수)
##각 게시판마다 views와 url을 분리할 예정


# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('index')

def honbabwrite(request):

    context = dict()

    #새 글 생성하기를 누르면 데이터베이스로 넘기기
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            temp_form = form.save(commit = False)   #당장 저장하지 말고 잠시 멈추고, temp form에 담음
            temp_form.category = "혼밥 게시판"  #사용자 선택을 어떻게 반영하지(아직 미구현)
            form.save()
            return redirect('index')

    #새 글을 입력받는 form을 띄워주기
    else:
        context['form'] = BlogModelForm()
    return render(request, 'honbabwrite.html', context) 

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

#상세페이지 함수
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

#프로필 함수
def honbabmyprofile(request):
    return render(request, 'honbabmyprofile.html')

def honcafemyprofile(request):
    return render(request, 'honcafemyprofile.html')

def honsulmyprofile(request):
    return render(request, 'honsulmyprofile.html')

def honnolmyprofile(request):
    return render(request, 'honnolmyprofile.html')