from django import forms

choices = (
    ('1', ''),
    ('2', ''),
    ('3', ''),
    ('4', ''),
    ('5', ''),
)

		
class FeedbackForm(forms.Form):
	Punctuality = forms.IntegerField(label='', widget=forms.RadioSelect(
		choices=choices), required=True)
	Subject_knowledge = forms.IntegerField(label='', widget=forms.RadioSelect(
		choices=choices), required=True)
	Behavior = forms.IntegerField(label='', widget=forms.RadioSelect(
		choices=choices), required=True)
	Method_of_teaching = forms.IntegerField(label='', widget=forms.RadioSelect(
		choices=choices), required=True)
	Audibility = forms.IntegerField(label='', widget=forms.RadioSelect(
		choices=choices), required=True)
	Syllabus_coverage = forms.IntegerField(label='', widget=forms.RadioSelect(
		choices=choices), required=True)
