from django.shortcuts import render

def say_hello(request):
    return render(request, 'hello.html')

def another_page(request):
    return render(request, 'another_page.html')