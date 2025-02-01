from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-sm px-3 py-2 focus:outline-none focus:ring focus:ring-green-300',
                'id': 'name',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-sm px-3 py-2 focus:outline-none focus:ring focus:ring-green-300',
                'id': 'email',
                'placeholder': 'Enter your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-sm px-3 py-2 focus:outline-none focus:ring focus:ring-green-300',
                'id': 'message',
                'rows': 4,
                'placeholder': 'Enter your message'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'focus:outline-none focus:ring focus:ring-green-300 w-full border border-gray-300 rounded-sm px-3 py-2',
                'id': 'phone',
                'placeholder': 'Enter your phone number'
            }),
        }