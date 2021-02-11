from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
from django.db.models import Count

from attendance.models import Attendance


class StaffAnalyticsListView(ListView):
    template_name = 'staff_analytics/staff_analytics_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(StaffAnalyticsListView, self).get_context_data(**kwargs)
        staffs = ctx['object_list']
        total_salary = 0
        total_students = 0
        for staff in staffs:
            print(staff)
            total_salary += staff['teacher__salary']
            total_students += staff['students_count']
        ctx['total_salary'] = total_salary
        ctx['total_students'] = total_students
        return ctx

    def get_queryset(self):
        staffs = Attendance.objects.filter(teacher__salary__gte=10000).values('teacher__firstname', 'teacher__salary').order_by('teacher__id').annotate(students_count=Count('student'))
        # for staff in staffs:
        #     if staff.salary > 100000:
        #         staffs['students_count'] = len(staff.students)
        #     else:
        #         staffs['students_count'] = 0
        # print(staffs)
        # print(Attendance.objects.values('teacher__firstname',))
        return staffs

class StaffAnalyticsDetailView(DetailView):
    model = Attendance
    template_name = "staff_analytics/staff_analytics_detail.html"
