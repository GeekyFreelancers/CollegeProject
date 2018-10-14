from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Section, Subject, Teacher, TeacherSubjectMapping, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'section', 'Punctuality',
                    'Subject_knowledge', 'Behaviour', 'Method_of_teaching',
                    'Audibility', 'Syllabus_coverage',)
    search_fields = ('teacher__teacher_name',)
    list_filter = ('teacher',)
    actions = None   # disables actions dropbox with delete action
    list_display_links = None

    def has_add_permission(self, request):
        return False


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'paper_id',)
    search_fields = ('subject_name', 'paper_id',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'teacher_dept',)
    search_fields = ('teacher_name',)


class TeacherSubjectMappingAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'subject_name',)
    search_fields = ('teacher_name__teacher_name',)
    list_filter = ('teacher_name', 'subject_name')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'year', 'branch', 'shift',)
    search_fields = ('section_name',)


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubjectMapping, TeacherSubjectMappingAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
