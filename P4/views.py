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

def url_path(request,name):
    return HttpResponse("<h1> welcome {}</h1>".format(name))

def ab(request,ab):
    a=ab.split(" ")
    sum=int(a[0])+int(a[1])
    return HttpResponse(sum)

def ab1(request,a,b):
    sum=int(a)-int(b)
    return HttpResponse(sum)

def greater_2(request,a,b):
    if a>b:
        return HttpResponse("The greatest value is {}".format(a))
    elif b>a:
        return HttpResponse("The greatest value is {}".format(b))
    else:
        return HttpResponse("Both the values are equal")

def greater_3(request,a,b,c):
    if a>b and a>c:
        return HttpResponse("The greatest value is {}".format(a))
    elif b>a and b>c:
        return HttpResponse("The greatest value is {}".format(b))
    elif c>a and c>b:
        return HttpResponse("The greatest value is {}".format(c))
    else:
        return HttpResponse("all the values are equal")