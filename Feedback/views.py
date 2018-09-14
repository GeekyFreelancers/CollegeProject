from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms import formset_factory

from .forms import FeedbackForm
from .models import Section
from .utils import form_is_incomplete, update_or_create_feedback_instance


def Feedback_form_Page(request, class_name):
    section = get_object_or_404(Section, section_name=class_name)
    teacher_with_subject = section.subjects.all()
    # It creates the no. of forms equals to the no. of teachers
    feedback_formset = formset_factory(
        FeedbackForm, extra=teacher_with_subject.count())
    error = False
    if request.method == 'POST':
        Formset = feedback_formset(request.POST)
        if Formset.is_valid():
            # It contains the `list of forms` in form of `list of dictionaries`
            actual_data = Formset.cleaned_data
            if form_is_incomplete(actual_data):
                Iterators = zip(teacher_with_subject, Formset)
                return render(
                    request, 'Feedback/feedback.html',
                    {'Iterators': Iterators, 'formset': Formset, 'error': True}
                )
            update_or_create_feedback_instance(actual_data,
                                               teacher_with_subject, section)
            return HttpResponseRedirect('/')
        else:
            error = True
    else:
        Formset = feedback_formset()
    Iterators = zip(teacher_with_subject, Formset)
    return render(
        request, 'Feedback/feedback.html',
        {'Iterators': Iterators, 'formset': Formset, 'error': error})
