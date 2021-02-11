from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import SiteConfig, AcademicSession, AcademicTerm
from .forms import SiteConfigForm, AcademicTermForm, AcademicSessionForm, CurrentSessionForm

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


class SessionListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicSession
    template_name = 'core/session_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AcademicSessionForm()
        return context



class SessionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = AcademicSession
  form_class = AcademicSessionForm
  template_name = 'core/mgt_form.html'
  success_url = reverse_lazy('sessions')
  success_message = 'New session successfully added'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Add new session'
      return context



class SessionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = AcademicSession
  form_class = AcademicSessionForm
  success_url = reverse_lazy('sessions')
  success_message = 'Session successfully updated.'
  template_name = 'core/mgt_form.html'

  def form_valid(self, form):
    obj = self.object
    if obj.current == False:
      terms = AcademicSession.objects.filter(
          current=True).exclude(name=obj.name).exists()
      if not terms:
        messages.warning(self.request, 'You must set a session to current.')
        return redirect('session-list')
    return super().form_valid(form)


class SessionDeleteView(LoginRequiredMixin, DeleteView):
  model = AcademicSession
  success_url = reverse_lazy('sessions')
  template_name = 'core/core_confirm_delete.html'
  success_message = "The session {} has been deleted with all its attached content"


  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      if obj.current == True:
        messages.warning(request, 'Cannot delete session as it is set to current')
        return redirect('sessions')
      messages.success(self.request, self.success_message.format(obj.name))
      return super(SessionDeleteView, self).delete(request, *args, **kwargs)


class TermListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = AcademicTerm
  template_name = 'core/term_list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = AcademicTermForm()
      return context


class TermCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = AcademicTerm
  form_class = AcademicTermForm
  template_name = 'core/mgt_form.html'
  success_url = reverse_lazy('terms')
  success_message = 'New term successfully added'



class TermUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = AcademicTerm
  form_class = AcademicTermForm
  success_url = reverse_lazy('terms')
  success_message = 'Term successfully updated.'
  template_name = 'core/mgt_form.html'


  def form_valid(self, form):
    obj = self.object
    if obj.current == False:
      terms = AcademicTerm.objects.filter(current=True).exclude(name=obj.name).exists()
      if not terms:
        messages.warning(self.request, 'You must set a term to current.')
        return redirect('term')
    return super().form_valid(form)


class TermDeleteView(LoginRequiredMixin, DeleteView):
  model = AcademicTerm
  success_url = reverse_lazy('terms')
  template_name = 'core/core_confirm_delete.html'
  success_message = "The term {} has been deleted with all its attached content"


  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      if obj.current == True:
        messages.warning(request, 'Cannot delete term as it is set to current')
        return redirect('terms')
      messages.success(self.request, self.success_message.format(obj.name))
      return super(TermDeleteView, self).delete(request, *args, **kwargs)

@login_required
def current_session_view(request):
  """ Current SEssion and Term """
  if request.method == 'POST':
    form = CurrentSessionForm(request.POST)
    if form.is_valid():
      session = form.cleaned_data['current_session']
      term = form.cleaned_data['current_term']
      AcademicSession.objects.filter(name=session).update(current=True)
      AcademicSession.objects.exclude(name=session).update(current=False)
      AcademicTerm.objects.filter(name=term).update(current=True)
      AcademicTerm.objects.exclude(name=term).update(current=False)

  else:
    form = CurrentSessionForm(initial={
      "current_session": AcademicSession.objects.get(current=True),
      "current_term": AcademicTerm.objects.get(current=True)
    })


  return render(request, 'core/current_session.html', {"form":form})
