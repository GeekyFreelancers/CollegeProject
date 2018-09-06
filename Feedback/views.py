from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms import formset_factory
from .forms import FeedbackForm
from .models import Section, Subject, Teacher, TeacherSubjectMapping, Feedback

# Create your views here.
def Feedback_form_Page(request, class_name):

	# It contains the instance of Section model which has section_name as class_name which is coming from url
	section = get_object_or_404(Section, section_name=class_name)

	# It contains the TeacherSubjectMapping instance of provided Section instance
	teacher_with_subject = section.subjects.all()

	# It creates the `extra` no. of forms ie it contains the forms which are equivalent to no. of teachers
	feedback_formset = formset_factory(FeedbackForm, extra=teacher_with_subject.count())
	if request.method == 'POST':
		Formset = feedback_formset(request.POST)
		if Formset.is_valid():
			# actual_data is in the form of list of dictionaries where 
			# each dictionary contains the data of each form in formset
			actual_data = Formset.cleaned_data  
			Feedback_instance = Feedback.objects.all()
			for dictionary, teacher in zip(actual_data, teacher_with_subject):
				# following loop checks if there is already an instance of
				# feedback for given teacher and section.
				for feedback in Feedback_instance:
					if (teacher.teacher_name == feedback.teacher) and (section == feedback.section):
					   feedback.Punctuality += dictionary['Punctuality']
					   feedback.Subject_knowledge += dictionary['Subject_knowledge']
					   feedback.Behaviour += dictionary['Behaviour']
					   feedback.Method_of_teaching += dictionary['Method_of_teaching']
					   feedback.Audibility += dictionary['Audibility']
					   feedback.Syllabus_coverage += dictionary['Syllabus_coverage']
					   feedback.save()
					   break
				# the following would create new instance since there would be no entry with given
				# and section.
				else:
					new_instance = Feedback(
						teacher=teacher.teacher_name,
						section=section,
						Punctuality=dictionary['Punctuality'],
						Subject_knowledge=dictionary['Subject_knowledge'],
						Behaviour=dictionary['Behaviour'],
						Method_of_teaching=dictionary['Method_of_teaching'],
						Audibility=dictionary['Audibility'],
						Syllabus_coverage=dictionary['Syllabus_coverage']
						)
					new_instance.save()
			return HttpResponseRedirect('/')
		else:
			Formset.errors
	else:
		Formset = feedback_formset()
	Iterators = zip(teacher_with_subject, Formset)
	return render(request, 'Feedback/feedback.html', {'Iterators': Iterators, 'formset':Formset})

def Feedback_submit(request):
	return render(request, 'Feedback/submit.html')