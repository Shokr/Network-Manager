from django.test import TestCase

from shokrnet.ip_manager.forms import LocationForm


class LocationFormTests(TestCase):
    def test_forms(self):
        form_data = {
            "name": "something",
            "address": "somethingsomethingsomethingsomethingsomethingsomething",
            "geolocation": "12458989787, 54948489",
        }
        form = LocationForm(data=form_data)
        self.assertTrue(form.is_valid())
