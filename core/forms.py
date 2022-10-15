from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.forms import widgets

from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django import forms
from django.conf import settings





#from users.models import OtpCode

from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

from django import forms

class LoginForm(forms.Form):
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


# class ChangePasswordForm(forms.Form):

#     class Meta:
#         model = CustomUser
#         fields = ('password1', 'password2')
   

#     new_password1 = forms.CharField(
#         label="New password",
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'New password'
#             }
#         ),
#     )
#     new_password2 = forms.CharField(
#         label="Confirm password",
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Confirm password',
#             }
#         ),
#     )

#     def clean_new_password2(self):
#         password1 = self.cleaned_data['new_password1']
#         password2 = self.cleaned_data['new_password2']

#         if password1 and password2 and password1 != password2:
#             raise ValidationError(_('Passwords are not match'))
#         password_validation.validate_password(password2)
#         return password2

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


# class SignUpForm(UserCreationForm):


#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Username",
#                 "class": "form-control"
#             }
#         ))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder": "Email",
#                 "class": "form-control"
#             }
#         ))
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password",
#                 "class": "form-control"
#             }
#         ))
 
#     password2 = None
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1')

