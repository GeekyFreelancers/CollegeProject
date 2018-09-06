from django.contrib import admin
from .models import Section, Subject, Teacher, TeacherSubjectMapping, Feedback

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(TeacherSubjectMapping)
admin.site.register(Section)
admin.site.register(Feedback)