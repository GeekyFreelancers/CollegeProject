from django.contrib import admin
from .models import Section, Subject, Teacher, TeacherSubjectMapping

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(TeacherSubjectMapping)
admin.site.register(Section)