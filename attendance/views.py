from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Attendance


class AttendanceListView(ListView):
    model = Attendance


class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = "attendance/attendance_detail.html"


class AttendanceCreateView(SuccessMessageMixin, CreateView):
    model = Attendance
    fields = '__all__'
    success_message = 'New attendance successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(AttendanceCreateView, self).get_form()
        form.fields['date'].widget = widgets.DateInput(
            attrs={'type': 'datetime-local'})
        return form


class AttendanceUpdateView(SuccessMessageMixin, UpdateView):
    model = Attendance
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(AttendanceUpdateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'datetime-local'})
        return form

class AttendanceDeleteView(DeleteView):
  model = Attendance
  success_url = reverse_lazy('attendance-list')
