from turtle import textinput
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required = True, widget=forms.TextInput(attrs={'placeholder': 'Introduce tu nombre', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', required = True, widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu e-mail', 'class': 'form-control'}))
    content = forms.CharField(label='Contenido', required = True, widget=forms.Textarea(attrs={'placeholder': 'Mándanos tu mensaje', 'class': 'form-control', 'rows': 3}))
