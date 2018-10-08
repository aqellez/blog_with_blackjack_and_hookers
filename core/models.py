from django.db import models
from django.contrib.auth.models import User


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(hidden=False)


class Tag(models.Model):
    word = models.CharField(max_length=40)

    def __str__(self):
        return self.word


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publication_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='articles')
    hidden = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    objects = ArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publication_date"]


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.TextField()
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.body[:20]

    class Meta:
        ordering = ["-publication_date"]
