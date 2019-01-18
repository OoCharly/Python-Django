from django.shortcuts import render
from django.views import View
from .models import *


class Mozaic(View):

    def get(self, request):
        files = File.objects.all()
        form = FileForm()
        return render(request, 'mozaic/index.html', {'form': form, 'files': files})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        files = File.objects.all()
        if form.is_valid():
            form.save()
        return render(request, 'mozaic/index.html', {'form': form, 'files': files})
