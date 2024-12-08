from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Extend the default UserCreationForm to include the email field
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Profile form to edit user information (optional)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
