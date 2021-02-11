from django.db import models
from django.utils import timezone
from django.urls import reverse


class Attendance(models.Model):
  STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

  SHAPES = [
      ('oval', 'Oval'),
      ('rectangular', 'Rectangular'),
      ('canopy', 'Canopy'),
      ('elevated', 'Elevated')
  ]
  date                = models.DateTimeField(default=timezone.now)
  classroom           = models.ForeignKey('classroom.ClassRoom', on_delete=models.CASCADE, default=1, related_name='attendance_classroom')
  student             = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1, related_name='attendance_student')
  teacher             = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, default=1, related_name='attendance_teacher')

  def __str__(self):
    return f'{self.classroom} {self.student} {self.teacher}'

  def get_absolute_url(self):
    return reverse('attendance-detail', kwargs={'pk': self.pk})
