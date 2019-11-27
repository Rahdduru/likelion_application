from django.urls import path
import main.views

app_name='main'
urlpatterns = [
    path('main/layout', main.views.layout, name = 'layout'), #상속페이지
    path('', main.views.main, name= 'main'), #메인페이지, 들어가자마자 보이는 페이지
    path('main/introduce', main.views.introduce, name= 'introduce'), #소개페이지
    path('main/board', main.views.board, name= 'board'), #게시판페이지
    path('main/signin', main.views.signin, name= 'signin'), #로그인페이지
    path('main/signup', main.views.signup, name= 'signup'), #로그아웃페이지
]