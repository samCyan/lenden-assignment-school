from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Subject


class SubjectListView(ListView):
    model = Subject


class SubjectDetailView(DetailView):
    model = Subject
    template_name = "subject/subject_detail.html"


class SubjectCreateView(SuccessMessageMixin, CreateView):
    model = Subject
    fields = '__all__'
    success_message = 'New subject successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(SubjectCreateView, self).get_form()
        # form.fields['total_duration'].widget = widgets.DateTimeInput(
        #     attrs={'type': 'datetime-local'})
        # form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
        #                                                             'type': 'date'})
        # form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        # form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class SubjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Subject
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(SubjectUpdateView, self).get_form()
        # form.fields['total_duration'].widget = widgets.Du(
        #     attrs={'type': 'datetime-local'})
        # form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
        #                                                             'type': 'date'})
        # form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        # form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

class SubjectDeleteView(DeleteView):
  model = Subject
  success_url = reverse_lazy('subject-list')
