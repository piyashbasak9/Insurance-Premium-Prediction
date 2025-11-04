from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

# Form for email verification code input
class EmailVerificationForm(forms.Form):
    verification_code = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter verification code'
    }))