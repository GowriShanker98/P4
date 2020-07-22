"""P4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name="Index"),
    path('',views.first,name="First"),
    path('second/',views.second,name="Second"),
    path('third/',views.third,name="Third"),
    path('fourth/',views.fourth,name="Fourth"),
    path('fifth/',views.fifth,name="Fifth"),
    path('urls_path/<name>',views.url_path,name="urls_path"),
    path('ab/<ab>',views.ab,name="ab"),
    path('ab/<a>/<b>',views.ab1,name="ab1"),
    path('greater2/<a>/<b>',views.greater_2,name="greater of 2 numbers"),
    path('greater3/<a>/<b>/<c>',views.greater_3,name="greater of 3 numbers"),
]
