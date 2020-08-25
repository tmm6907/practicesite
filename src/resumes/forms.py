from django import forms
from .models import User, Education, Work

class ResumeForm(forms.ModelForm):
    class Meta:
        user_model      = User
        education_model = Education
        work_model      = Work

        fields = [
            'full name',
            'email address',
            'address',
            'phone',

            'level',
            'school name',
            'start year',
            'end year',
            'location',

            'position',
            'description',
            'start date',
            'end date',
        ]