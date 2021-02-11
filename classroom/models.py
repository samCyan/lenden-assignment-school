from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

# from subject import models as subject_models
# from staff import models as staff_models


class ClassRoom(models.Model):
  STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

  SHAPES = [
      ('oval', 'Oval'),
      ('rectangular', 'Rectangular'),
      ('canopy', 'Canopy'),
      ('elevated', 'Elevated')
  ]
  name                = models.CharField(max_length=50, default='UNASSIGNED')
  capacity            = models.IntegerField(blank=False, default=30)
  web_lecture         = models.CharField(max_length=20, choices=STATUS, default='Active')
  shape               = models.CharField(max_length=20, choices=SHAPES, default='Oval')
  subjects            = models.ManyToManyField('subject.Subject', default=[], related_name='classroom_subjects')
  teachers            = models.ManyToManyField('staff.Staff', default=[], related_name='classroom_teachers')


  def __str__(self):
    return f'{self.capacity} {self.web_lecture} {self.shape}'

  def get_absolute_url(self):
    return reverse('classroom-detail', kwargs={'pk': self.pk})
