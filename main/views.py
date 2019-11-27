from django.shortcuts import render

# Create your views here.

#상속페이지
def layout(request):
    return render(request, 'everyone/layout.html')

#페이지에 첫번째로 보이는 페이지
def main(request):
    return render(request, 'everyone/main.html')

#소개페이지
def introduce(request):
    return render(request, 'everyone/introduce.html')

#게시판 페이지
def board(request):
    return render(request, 'everyone/board.html')

#로그인 페이지
def signin(request):
    return render(request, 'everyone/signin.html')

#회원가입 페이지
def signup(request):
    return render(request, 'everyone/signup.html')