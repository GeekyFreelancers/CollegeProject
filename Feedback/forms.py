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

class FeedbackForm(forms.ModelForm):	
	class Meta:
		model = Feedback
		exclude=['teacher', 'section']
		widgets =	{
			'Punctuality': forms.RadioSelect(choices=choices,),
			'Subject_knowledge': forms.RadioSelect(choices=choices,),
			'Behaviour': forms.RadioSelect(choices=choices,),
			'Method_of_teaching': forms.RadioSelect(choices=choices,),
			'Audibility': forms.RadioSelect(choices=choices,),
			'Syllabus_coverage': forms.RadioSelect(choices=choices,)
		}
		