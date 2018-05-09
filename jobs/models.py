from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    tags = models.CharField(max_length=100)
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User,default=None)
    def __str__(self):
            return self.title 