from django.views.generic import ListView, DetailView
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
            total_salary += staff['teacher__salary']
            total_students += staff['students_count']
        ctx['total_salary'] = total_salary
        ctx['total_students'] = total_students
        return ctx

    def get_queryset(self):
        staffs = Attendance.objects.filter(teacher__salary__gte=100000).values('teacher__firstname', 'teacher__salary').order_by('teacher__id').annotate(students_count=Count('student'))
        return staffs


class StaffAnalyticsDetailView(DetailView):
    model = Attendance
    template_name = "staff_analytics/staff_analytics_detail.html"
