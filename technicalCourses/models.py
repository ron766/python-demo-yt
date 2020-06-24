from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class AllCourses(models.Model):
  coursename = models.CharField(max_length=200)
  insname = models.CharField(max_length=200)
  startedfrom = models.DateTimeField('Started from')

  def __str__(self):
    return self.coursename

  def was_published_recently(self):
    now = timezone.now()
    # return self.startedfrom >= timezone.now() - datetime.timedelta(days=1)
    return now - datetime.timedelta(days=1) <= self.startedfrom <= now

class Details(models.Model):
  course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
  # sp = models.CharField(max_length=500);
  # il = models.CharField(max_length=500);
  ct = models.CharField(max_length=500)
  your_choice = models.BooleanField(default=False)
  def __str__(self):
    return str(self.ct)
