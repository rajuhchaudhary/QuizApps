from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('demo/',views.demo,name='demo'),
    path('',views.home,name='home'),
    path('QuizOne/',views.am1,name='QuizOne'),
    path('QuizTwo/',views.am2,name='QuizTwo'),
    path('QuizThree/',views.am3,name='QuizThree'),
    path('QuizFour/',views.am4,name='QuizFour'),
    path('QuizFive/',views.am5,name='QuizFive'),
    path('QuizSix/',views.am6,name='QuizSix'),
    path('QuizSeven/',views.am7,name='QuizSeven'),
    path('QuizEight/',views.am8,name='QuizEight'),
    path('QuizNine/',views.am9,name='QuizNine'),
    path('QuizTen/',views.am10,name='QuizTen'),
    path('contact/',views.contact,name='contact')

]