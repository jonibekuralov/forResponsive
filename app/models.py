from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Resource.Status.Published)


class Resource(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    author = models.CharField(max_length=20)
    body = models.TextField()
    DocumentFile = models.FileField(upload_to='documentFile', blank=True, null=True)
    TestLink = models.URLField(max_length=160, blank=True, null=True)
    CrosswordLink = models.URLField(max_length=160, blank=True, null=True)
    YoutubeLink = models.URLField(max_length=160, blank=True, null=True)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                              )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email


class HomeModel(models.Model):
    CarouselImages = models.ImageField(upload_to='CarouselImages', blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.body


class footerData(models.Model):
    copyright = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Location(models.Model):
    location = models.URLField(max_length=600)

    def __str__(self):
        return self.location


class Libary(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.title
