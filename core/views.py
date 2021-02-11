from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView

from .models import SiteConfig
from .forms import SiteConfigForm


class IndexView(LoginRequiredMixin, TemplateView):
      template_name = 'index.html'


@login_required
def siteconfig_view(request):
  """ Site Config View """
  if request.method == 'POST':
    form = SiteConfigForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Configurations successfully updated')
      return HttpResponseRedirect('site-config')
  else:
    form = SiteConfigForm(queryset=SiteConfig.objects.all())

  context = {"formset": form, "title": "Configuration"}
  return render(request, 'core/siteconfig.html', context)

