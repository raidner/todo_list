from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        max_length=15,
        required=True,
        help_text='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Your password must contain at least 8 characters.',
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Enter your password again to confirm',
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()