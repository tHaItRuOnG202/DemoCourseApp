from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']
    list_per_page = 3


class CourseForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['avatar']
    form = CourseForm

    def avatar(self, courses):
        if courses:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=courses.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
