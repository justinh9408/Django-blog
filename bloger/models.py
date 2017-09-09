from django.db import models
# from ckeditor.fields import RichTextField
# Create your models here.

class Tag(models.Model):
    tag = models.CharField(verbose_name="标签",max_length=20)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.tag





class Article(models.Model):
    title = models.CharField(max_length=45, verbose_name='题目')
    content  = models.TextField(verbose_name='内容')
    date = models.DateField(auto_now_add=True)
    tag = models.ForeignKey('Tag')
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date']
    def __str__(self):
        return self.title
