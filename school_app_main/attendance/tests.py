from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Attendance
from classroom.models import ClassRoom
from staff.models import Staff
from student.models import Student


dt_string_format = "%d/%m/%Y"


class AttendanceTest(TestCase):
    def create_attendance(self, date=datetime.strptime("04/04/2017", "%d/%m/%Y")):
        classroom = ClassRoom.objects.create(name='classroom1', capacity=30, web_lecture=True, shape='Oval')
        student = Student.objects.create(current_status="Active", registration_number="12132", surname="xyz", firstname="abc", gender='Male')
        teacher = Staff.objects.create(current_status='Active',surname='surname1',firstname='firstname1',other_name='other_name1',
                     gender='Male',
                     date_of_birth=datetime.strptime("04/04/2017", "%d/%m/%Y"),
                     date_of_admission=datetime.strptime("25/01/2018", "%d/%m/%Y"),
                     salary=10000,mobile_number='1234567890',address='address1',
                     others='',takes_web_lecture=False)
        return Attendance.objects.create(date=date,classroom=classroom,student=student,teacher=teacher)

    def test_attendance_creation(self):
        a = self.create_attendance()
        self.assertTrue(isinstance(a, Attendance))
        self.assertEqual(str(a), f'{a.classroom} {a.student} {a.teacher}')

    def test_whatever_list_view(self):
        s = self.create_attendance()
        url = reverse("attendance-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(s.teacher.surname.encode(), resp.content)

