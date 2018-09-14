from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.db import transaction



class SignupForm(UserCreationForm):
    name = forms.CharField(required=False, label='name')
    phoneNumber = forms.CharField(required=False, label='phonenumber')
    identityNumber = forms.CharField(required=False, label='identity number')
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('name', 'phoneNumber', 'identityNumber')


    def save(self, commit=True):
        with transaction.atomic():
            user = super(SignupForm, self).save()
            user.refresh_from_db()
            user.profile.name = self.cleaned_data.get('name')
            user.profile.phoneNumber = self.cleaned_data.get('phoneNumber')
            user.profile.idnetityNumber = self.cleaned_data.get('idendtityNumber')
            user = super().save(False)
            user = super().save()
            return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

