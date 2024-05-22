from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    #Form data cleaning - Lower user inputs
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        return last_name

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user
