from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    word = models.CharField(max_length=15)

    def __str__(self):
        return self.word


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publication_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='articles')
    hidden = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["publication_date"]


