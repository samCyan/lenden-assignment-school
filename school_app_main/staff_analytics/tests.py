from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Staff


dt_string_format = "%d/%m/%Y"


class StaffTest(TestCase):
    def create_staff(self, current_status='Active',surname='surname1',firstname='firstname1',other_name='other_name1',
                     gender='Male',
                     date_of_birth=datetime.strptime("04/04/2017", "%d/%m/%Y"),
                     date_of_admission=datetime.strptime("25/01/2018", "%d/%m/%Y"),
                     salary=10000,mobile_num_regex='.*',mobile_number='1234567890',address='address1',
                     others='',takes_web_lecture=False,):
        return Staff.objects.create(current_status=current_status,surname=surname,firstname=firstname,
                                    other_name=other_name,gender=gender,date_of_birth=date_of_birth,
                                    date_of_admission=date_of_admission,salary=salary,
                                    mobile_number=mobile_number,
                                    address=address,others=others,
                                    takes_web_lecture=takes_web_lecture,)

    def test_staff_creation(self):
        s = self.create_staff()
        self.assertTrue(isinstance(s, Staff))
        self.assertEqual(str(s), f'{s.surname} {s.firstname} {s.other_name}')

    def test_whatever_list_view(self):
        s = self.create_staff()
        url = reverse("staff-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(s.firstname.encode(), resp.content)

