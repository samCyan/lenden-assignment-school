from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentTest(TestCase):

    def create_student(self, current_status="Active", registration_number="12132", surname="xyz", firstname="abc", gender='Male'):
        return Student.objects.create(current_status=current_status, registration_number=registration_number, surname=surname, firstname=firstname, gender=gender)

    def test_student_creation(self):
        s = self.create_student()
        self.assertTrue(isinstance(s, Student))
        self.assertEqual(str(s), f'{s.surname} {s.firstname} {s.other_name} ({s.registration_number})')

    def test_whatever_list_view(self):
        s = self.create_student()
        url = reverse("student-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(s.firstname.encode(), resp.content)

