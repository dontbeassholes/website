from django.db import models


# Create your models here.

class CategoryModel(models.Model):
    category_title = models.CharField(max_length=32)
    category_icon = models.FileField(upload_to='snob_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


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


class LibraryModel(models.Model):
    book_title = models.CharField(max_length=50, help_text='добавьте название вашего курса')
    book_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    book_pages = models.IntegerField(help_text='добавьте количество страниц в книге')
    book_description = models.TextField(help_text='добавьте описание к вашему курсу')
    book_image = models.FileField(upload_to='snob_images')
    book_author = models.CharField(max_length=50, help_text='фамилия и имя автора')

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=50, help_text='добавьте имя и фамилию преподавателя')
    teacher_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    teacher_experience = models.IntegerField(help_text='какой опыт работы учителя?')
    teacher_profession = models.TextField(help_text='что преподает этот учитель?')
    teacher_image = models.FileField(upload_to='snob_images')

    def __str__(self):
        return self.teacher_name

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
