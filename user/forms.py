from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from user.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254, help_text='Required. Enter the valid email.',
                             required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()

        if not any(i in email for i in ('.ru', '.com', '.ua', '.net')):
            raise forms.ValidationError('Enter the valid email')

        if user_count > 0:
            raise forms.ValidationError('A user with that email already exists.')
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not any(i in email for i in ('.ru', '.com', '.ua', '.net')):
            raise forms.ValidationError('Enter the valid email')
        return email


class ProfileUpdateForm(forms.ModelForm):
    about = forms.CharField(required=False,
                            widget=forms.Textarea(
                                attrs=
                                {'class': 'form-control', 'rows': 5, 'cols': 5}
                            ))

    class Meta:
        model = Profile
        fields = ('profile_name', 'image', 'about',)
