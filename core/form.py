from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from core.models import Record

class sign_up_form(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class Edit_Record(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(Edit_Record, self).__init__(*args, **kwargs)
        # Add Tailwind CSS classes to form fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'border rounded-lg p-2 w-full'})  # Add Tailwind CSS classes here  # Assuming you're using Bootstrap, change 'form-control' to your desired CSS class