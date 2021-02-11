from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator
# from subject import models as subject_models


class Staff(models.Model):
  STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

  current_status      = models.CharField(max_length=10, choices=STATUS, default='active')
  surname             = models.CharField(max_length=200)
  firstname           = models.CharField(max_length=200)
  other_name          = models.CharField(max_length=200, blank=True)
  gender              = models.CharField(max_length=10, choices=GENDER, default='male')
  date_of_birth       = models.DateField(default=timezone.now)
  date_of_admission   = models.DateField(default=timezone.now)
  salary              = models.IntegerField(blank=False, default=5000)
  mobile_num_regex    = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
  mobile_number       = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)
  subjects            = models.ManyToManyField('subject.Subject')
  address             = models.TextField(blank=True)
  others              = models.TextField(blank=True)
  takes_web_lecture   = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.surname} {self.firstname} {self.other_name}'

  def get_absolute_url(self):
    return reverse('staff-detail', kwargs={'pk': self.pk})
