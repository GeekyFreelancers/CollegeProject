from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from .forms import FeedbackForm
from .models import Section, Subject, Teacher, TeacherSubjectMapping

# Create your views here.
def Feedback_form_Page(request, class_name):
	section = get_object_or_404(Section, section_name=class_name)
	teacher_with_subject = section.subjects.all()
	feedback_formset = formset_factory(FeedbackForm, extra=teacher_with_subject.count())
	Formset = feedback_formset()
	Iterators = zip(teacher_with_subject, Formset)
	return render(request, 'Feedback/feedback.html', {'Iterators': Iterators})
