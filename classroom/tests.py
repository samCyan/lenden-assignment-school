from django.test import TestCase
from django.urls import reverse

from .models import ClassRoom


class ClassRoomTest(TestCase):
    def create_classroom(self,name='class1',capacity=30,web_lecture='Active',shape='Oval'):
        return ClassRoom.objects.create(name=name,capacity=capacity,web_lecture=web_lecture,shape=shape)

    def test_classroom_creation(self):
        c = self.create_classroom()
        self.assertTrue(isinstance(c, ClassRoom))
        self.assertEqual(str(c), f'{c.capacity} {c.web_lecture} {c.shape}')

    def test_whatever_list_view(self):
        c = self.create_classroom()
        url = reverse("classroom-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(c.name.encode(), resp.content)

