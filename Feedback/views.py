from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms import formset_factory

from .forms import FeedbackForm
from .models import Section, Feedback, Teacher
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

def Feedback_submit(request):
    return render(request, 'Feedback/submit.html')
    
def teacher_check(request):
    feedback = Feedback.objects.all()
    teacher = Teacher.objects.all()
    if request.method=='POST':
        faculty_name = request.POST['dropdown1']
        dept_name = request.POST['dropdown']
        for t in feedback:
            if(t.teacher.teacher_name == faculty_name and t.teacher.teacher_dept == dept_name):
                Flag = 1
                break
            else:
                Flag = 0
                continue
        return render(request,'Feedback/teacher_check.html',{'Feedback' : feedback, 'department' : dept_name, 'faculty' : faculty_name, 'Flag': Flag,'teacher':teacher})
    else:
        return render(request, 'Feedback/teacher_check.html',{'teacher':teacher})