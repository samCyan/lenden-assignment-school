
from django.forms import modelformset_factory

from .models import SiteConfig

SiteConfigForm = modelformset_factory(SiteConfig, fields=('key', 'value'), extra=0)
