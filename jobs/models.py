from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jobs:jobs_by_category', args=[self.slug])



class Job(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    category = models.ForeignKey(JobCategory, null=True, on_delete=models.CASCADE)
    description = RichTextField(blank=True)
    tags = models.CharField(max_length=100)
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
            return self.title 