from django import forms
from django.forms import ModelForm
from .models import Book
from .models import WishList
from .models import ForumPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={ "class" : "form-control", "placeholder": "e.g New World"}))
    web = forms.URLField(widget=forms.URLInput(attrs={ "class" : "form-control", "placeholder": "e.g www.a@a.com"}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={ "class" : "form-control","placeholder": "e.g 0.32"}))
    picture = forms.FileField(widget=forms.FileInput(attrs={"class":"btn btn-transparent form-control-file"}))
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]
class WishListForm(ModelForm):
    book = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"e.g New World"}))
    class Meta:
        model = WishList
        fields = [
            'book',
        ]

class PostForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"e.g Hello John!"}))
    class Meta:
        model = ForumPost
        fields = [
            'body',
        ]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ] 
    def __init__(self, *args,**kwargs):
            super(SignUpForm, self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'

