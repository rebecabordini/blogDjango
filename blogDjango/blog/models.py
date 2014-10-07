from django.db import models
from django.db.models import permalink
from django.utils import timezone
import datetime


class BlogManager(models.Manager):
    def posts_publicados_no_passado(self):
        return self.filter(posted__lte=datetime.datetime.now())

    def posts_publicados_no_futuro(self):
        return self.filter(posted__gt=datetime.datetime.now())


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True)
    category = models.ForeignKey('blog.Category')
    objects = BlogManager()

    def __unicode__(self):
        return '%s' % self.title

    def get_data_publicacao(self):
        return self.posted

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })



