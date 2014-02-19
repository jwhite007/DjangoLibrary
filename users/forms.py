from django.forms import ModelForm
# from django import forms
from .models import users


class UsersForm(ModelForm):
    class Meta:
        model = users
        fields = ('first_name', 'last_name', 'eddress')
        # exclude = ('timestamp')
