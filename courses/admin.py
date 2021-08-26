from django.contrib import admin
from courses.models import Course,Module,Subject
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Subject)
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display=['title','slug']
    prepopulated_fields={'slug':('title',)}

class ModuleInline(admin.StackedInline):
    model=Module

class CourseAdmin(admin.ModelAdmin):
    list_display=['title', 'subject', 'created']
    list_filter=['created', 'subject']
    search_field=['title', 'overview']
    prepopulated_fields={'slug':('title',)}
    inlines=[ModuleInline]
