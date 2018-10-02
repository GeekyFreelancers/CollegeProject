from .models import Feedback


def form_is_incomplete(list_of_forms):
    for form in list_of_forms:
        if len(form) == 0:
            break
    else:
        return False
    return True


def update_or_create_feedback_instance(list_of_forms, teacher_with_subject,
                                       section):
    Feedback_instance = Feedback.objects.all()
    for form, teacher in zip(list_of_forms, teacher_with_subject):
        # following loop checks if there is already an instance of feedback for
        # given teacher and section.
        for feedback in Feedback_instance:
            if (teacher.teacher_name == feedback.teacher and
                    section == feedback.section):
                feedback.Punctuality += form['Punctuality']
                feedback.Subject_knowledge += form['Subject_knowledge']
                feedback.Behaviour += form['Behaviour']
                feedback.Method_of_teaching += form['Method_of_teaching']
                feedback.Audibility += form['Audibility']
                feedback.Syllabus_coverage += form['Syllabus_coverage']
                feedback.save()
                break
        # the following would create new instance if there is no entry with
        # given teacher and section.
        else:
            new_instance = Feedback(
                teacher=teacher.teacher_name,
                section=section,
                Punctuality=form['Punctuality'],
                Subject_knowledge=form['Subject_knowledge'],
                Behaviour=form['Behaviour'],
                Method_of_teaching=form['Method_of_teaching'],
                Audibility=form['Audibility'],
                Syllabus_coverage=form['Syllabus_coverage']
            )
            new_instance.save()
