from django.contrib import admin

from snob.models import CategoryModel, CourseModel, LibraryModel, TeacherModel


# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at', 'category_icon']
    search_fields = ['category_title']
    list_filter = ['created_at']
    ordering = ['category_title']


@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'course_category', 'course_price', 'course_duration', 'course_description', 'course_image', 'course_teacher', 'course_created_at']
    search_fields = ['course_title']
    list_filter = ['course_created_at']
    ordering = ['course_title']

@admin.register(LibraryModel)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'book_category', 'book_pages', 'book_description', 'book_image', 'book_author']
    search_fields = ['book_title']
    ordering = ['book_title']

@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'teacher_category', 'teacher_experience', 'teacher_profession', 'teacher_image']
    search_fields = ['teacher_name']
    ordering = ['teacher_name']
