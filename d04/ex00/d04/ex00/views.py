from django.shortcuts import render, HttpResponse


def ex00(request):
    return render(request, 'ex00/index.html')
# Create your views here.
