from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class SpotlightArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(spotlight=True)[:4]


class Article(models.Model):
    pub_date = models.DateTimeField("date published")
    title = models.CharField(max_length=120)
    media_name = models.CharField(max_length=120)
    short_desc = models.CharField(max_length=200)
    article_text = models.TextField()
    embed_text = models.TextField()
    spotlight = models.BooleanField(default=False)
    tags = TaggableManager()

    objects = models.Manager()
    spotlight_objects = SpotlightArticleManager()
    
    def __str__(self):
        return f"{self.media_name}"
