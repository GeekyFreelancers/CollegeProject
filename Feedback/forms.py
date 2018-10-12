from django import forms
from django.forms import ModelForm

from .models import Feedback

choices = (
    ('1', ''),
    ('2', ''),
    ('3', ''),
    ('4', ''),
    ('5', ''),
)


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['teacher', 'section']
        widgets = {'Punctuality': forms.RadioSelect(choices=choices, attrs={'class': 'star'}),
                   'Subject_knowledge': forms.RadioSelect(choices=choices, attrs={'class': 'star'}),
                   'Behaviour': forms.RadioSelect(choices=choices, attrs={'class': 'star'}),
                   'Method_of_teaching': forms.RadioSelect(choices=choices, attrs={'class': 'star'}),
                   'Audibility': forms.RadioSelect(choices=choices, attrs={'class': 'star'}),
                   'Syllabus_coverage': forms.RadioSelect(choices=choices, attrs={'class': 'star'})}
