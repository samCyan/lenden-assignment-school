from django.db import models
from django.urls import reverse


class Subject(models.Model):

  name                = models.CharField(max_length=100, blank=False, default='')
  chapters            = models.IntegerField(blank=False, default=1)
  total_duration      = models.DurationField()
  per_class_duration  = models.DurationField()
  classroom           = models.ForeignKey('classroom.ClassRoom', on_delete=models.CASCADE, default=1)


  def __str__(self):
    return f'{self.name}'

  def get_absolute_url(self):
    return reverse('subject-detail', kwargs={'pk': self.pk})
