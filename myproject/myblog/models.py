from django.db import models
from django import forms

# Create your models here.

class MyBlogPost(models.Model):
    title = models.CharField(max_length=255)    ##博文的title，限制该字段最大长度为255
    body = models.TextField()    ##博文正文数据较长文本，使用TextField类型
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


class MyBlogPostForm(forms.ModelForm):

    class Meta:
        model = MyBlogPost
        exclude = ('timestamp',)
