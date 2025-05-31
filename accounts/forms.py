from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','image','bio','password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FIrst name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'bio' : forms.Textarea(attrs={'class': 'form-control','rows': '5', 'placeholder': 'Bio'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
        }

class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }
