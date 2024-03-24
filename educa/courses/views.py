from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    template = 'courses/index.html'
    return render(request, template, context)