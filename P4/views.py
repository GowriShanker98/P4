from django.http import HttpResponse
from django.shortcuts import render

#Create your views here
def index(request):
    return HttpResponse("Welcome to Index Page")

def first(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"Gowri",'name':"Shanker"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",context={'Fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",context={'a':10,'b':20})
