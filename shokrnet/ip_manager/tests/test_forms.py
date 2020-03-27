from django.test import TestCase

from ..froms import *


class SiteFormTests(TestCase):
    def test_forms(self):
        form_data = {'name': 'something',
                     'address': 'somethingsomethingsomethingsomethingsomethingsomething',
                     'geolocation': '12458989787, 54948489'}
        form = SiteForm(data=form_data)
        self.assertTrue(form.is_valid())
