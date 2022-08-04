from django.shortcuts import render
"""뷰의 이름 규칙
그냥 렌더를 위한 단순 뷰면은 해당 html의 이름으로 정함
렌더말고도 다른 기능이 있으면 "기능_html이름"으로 짓는다.
"""
def index(request):
    return render(request, "index.html")

def map(request):
    pass