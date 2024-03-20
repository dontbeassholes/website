from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    category_title = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'course category'
        verbose_name_plural = 'course categories'


class CourseModel(models.Model):
    course_title = models.CharField(max_length=50, help_text='добавьте название вашего курса')
    course_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    course_price = models.FloatField()
    course_duration = models.CharField(max_length=30, help_text='добавьте продолжительность вашего курса')
    course_description = models.TextField(help_text='добавьте описание к вашему курсу')
    course_image = models.FileField(upload_to='snob_images')
    course_teacher = models.CharField(max_length=50, help_text='фамилия и имя преподавателя данного курса')
    course_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_title


    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'