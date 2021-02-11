from django.db import models


class SiteConfig(models.Model):
  """ Site Configurations """
  key = models.SlugField()
  value = models.CharField(max_length=200)

  def __str__(self):
    return self.key


