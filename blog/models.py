from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 摘要最大长度70，可以为空
    excerpt = models.CharField(max_length=70, blank=True)
    # 一篇文章对应一个分类，但一个分类可以对应多个文章，使用一对多关系ForeignKey
    category = models.ForeignKey(Category)
    # 一篇文章可以有多个标签，同一个标签下也可能有多篇文章，使用多对多关系ManyToManyField
    tags = models.ManyToManyField(Tag, blank=True)
    # 使用内置的User模型
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        """生成detail视图函数需要的网址"""
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']