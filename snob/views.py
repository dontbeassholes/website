from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, template_name='index.html')

def contact(request):
    return render(request, template_name='contact.html')

def courses(request):
    return render(request, template_name='courses.html')

def elements(request):
    return render(request, template_name='elements.html')

def news(request):
    return render(request, template_name='news.html')

def news_post(request):
    return render(request, template_name='news_post.html')

def teachers(request):
    return render(request, template_name='teachers')

def index(request):
    return render(request, template_name='index.html')