""" Forms Module """
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django_select2 import forms as s2forms
from .models import Task, KRA, Metric


class CustomLoginForm(AuthenticationForm):
    """ Create custom login form for adding styling classes """
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))

    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

class KeyWidget(s2forms.Select2Widget):
    search_fields = ['category__icontains',]
    attrs = {'data-placeholder': 'Search for MyModel values',}

class MetricWidget(s2forms.Select2MultipleWidget):
    search_fields = ['description__icontains',]

class TaskForm(forms.ModelForm):
    """ Custom Form for Task Creation and using select2 widgets """

    class Meta:
        model = Task
        fields = ['key_area', 'metric', 'description']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['metric'].queryset = Metric.objects.none()


    