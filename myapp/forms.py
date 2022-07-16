from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class UsersLog(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'password']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


