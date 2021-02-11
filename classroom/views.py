from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ClassRoom


class ClassRoomListView(ListView):
    model = ClassRoom


class ClassRoomDetailView(DetailView):
    model = ClassRoom
    template_name = "classroom/classroom_detail.html"


class ClassRoomCreateView(SuccessMessageMixin, CreateView):
    model = ClassRoom
    fields = '__all__'
    success_message = 'New classroom successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(ClassRoomCreateView, self).get_form()
        return form


class ClassRoomUpdateView(SuccessMessageMixin, UpdateView):
    model = ClassRoom
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(ClassRoomUpdateView, self).get_form()
        return form

class ClassRoomDeleteView(DeleteView):
  model = ClassRoom
  success_url = reverse_lazy('classroom-list')
