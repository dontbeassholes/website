from django.contrib import admin

from snob.models import CategoryModel, CourseModel


# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']
    ordering = ['category_title']


@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'course_category', 'course_price', 'course_duration', 'course_description', 'course_image', 'course_teacher', 'course_created_at']
    search_fields = ['course_title']
    list_filter = ['course_created_at']
    ordering = ['course_title']
