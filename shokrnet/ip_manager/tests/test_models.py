from django.test import TestCase

from ..models import *


class TestIPAddress(TestCase):
    def test_ips(self):
        ips = IPAddress.objects.bulk_create(
            (
                IPAddress(family=4, address="192.0.2.1/24"),
                IPAddress(family=4, address="192.0.2.2/24"),
                IPAddress(family=4, address="192.0.2.3/24"),
            )
        )


class TestVLAN(TestCase):
    def test_get_next_available_vid(self):
        vlan = VLAN.objects.create(name="VLAN", vid=10)
        VLAN.objects.bulk_create(
            (
                VLAN(name="VLAN 1", vid=1),
                VLAN(name="VLAN 2", vid=2),
                VLAN(name="VLAN 3", vid=3),
                VLAN(name="VLAN 5", vid=5),
            )
        )
