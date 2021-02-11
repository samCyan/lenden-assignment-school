import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Subject
from classroom.models import ClassRoom


class SubjectTest(TestCase):
    def create_subject(self, name="subject1", chapters=25, total_duration=datetime.timedelta(hours=90),
                       per_class_duration=datetime.timedelta(hours=9)):
        classroom = ClassRoom.objects.create(name='classroom1', capacity=30, web_lecture=True,
                                      shape='Oval')
        return Subject.objects.create(name=name, chapters=chapters, total_duration=total_duration,
                                      per_class_duration=per_class_duration, classroom=classroom)

    def test_subject_creation(self):
        s = self.create_subject()
        self.assertTrue(isinstance(s, Subject))
        self.assertEqual(str(s), f'{s.chapters} ')

    def test_whatever_list_view(self):
        s = self.create_subject()
        url = reverse("subject-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(s.name.encode(), resp.content)

