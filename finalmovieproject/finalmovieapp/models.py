import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering= ('name', )
        verbose_name='category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('finalmovieapp:movie_by_category', args=[self.slug])
    #go to /category page

    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(1968, datetime.date.today().year + 1)]
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    desc = models.TextField()
    date = models.IntegerField(choices=YEAR_CHOICES)
    image = models.ImageField(upload_to='movies',blank=True)
    actors = models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    youtubelink = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def get_url(self):
        return reverse('finalmovieapp:moviesCatDetail', args=[self.category.slug,self.slug])
    # go to /category/product page

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.movie.name, self.name)
