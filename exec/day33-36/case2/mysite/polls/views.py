from django.shortcuts import render,HttpResponse

# Create your views here.
#用户发来的第一个请求作为第一个参数传递给函数，形参就是request
def index(request):
    return HttpResponse('<h1>Hello Django</h1>')
