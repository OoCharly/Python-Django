from django.db import models
from django import forms


class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files')


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['name', 'file']
