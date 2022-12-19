from django import forms
from django.forms import ModelForm
from .models import Student



class StudentForm(forms.ModelForm):
  class Meta:
    model = Student

    fields = ['studentnumber', 'lastname', 'firstname', 'telephone', 'email', 'fieldofstudy', 'gpa']

    labels = {
      'studentnumber': 'Student Number', 
      'lastname': 'Last Name', 
      'firstname': 'First Name', 
      'telephone': 'Telephone',
      'email': 'Email', 
      'fieldofstudy': 'Field of Study', 
      'gpa': 'GPA'
    }

    widgets = {
      'studentnumber': forms.NumberInput(attrs={'class': 'form-control'}), 
      'lastname': forms.TextInput(attrs={'class': 'form-control'}),
      'firstname': forms.TextInput(attrs={'class': 'form-control'}),
      'telephone': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'fieldofstudy': forms.TextInput(attrs={'class': 'form-control'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
    }
