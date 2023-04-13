from django.shortcuts import HttpResponse, redirect

# Create your views here.

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my project')

def redirect_to_time_view(request):
    if request.method == 'GET':
        return redirect('https://time.is/ru/Bishkek')

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


