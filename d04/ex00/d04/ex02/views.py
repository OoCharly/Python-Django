from django.conf import settings
from django import forms
from django.shortcuts import render
import os
import datetime


history = getattr(settings, "HISTORY_FILE", None)
if not history:
    history = 'default.log'


class myForm(forms.Form):
    msg = forms.CharField(label="message", required=True)


def read_history():
    out = []
    if os.path.isfile(history):
        with open(history, 'r') as file:
            out = file.readlines()
    return out


def append_history(msg):
    try:
        file = open(history, 'a')
    except FileNotFoundError:
        file = open(history, 'w')
    file.write(msg + '\n')
    file.close()


def ex02(request):
    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S : ")
            msg = form.cleaned_data['msg']
            append_history(str(date) + msg)
    else:
        form = myForm()
    old = read_history()
    return render(request, 'ex02/form.html', {'form': form, 'msgs': old})
# Create your views here.
