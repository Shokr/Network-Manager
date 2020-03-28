import ipaddress

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .constants import *
from .validators import DNSValidator


class Location(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    geolocation = models.CharField(max_length=100, blank=True, null=True)

    time_created = models.DateTimeField(auto_created=True, default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'Locations'
        ordering = ['name']
        verbose_name = 'Network Location'
        verbose_name_plural = 'Network Locations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ip_manager:Location', args=[self.pk])


class DeviceType(models.Model):
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    model_number = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=64)

    time_created = models.DateTimeField(auto_created=True, default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'device_types'
        ordering = ['name']
        verbose_name = 'Device Type'
        verbose_name_plural = 'Device Types'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ip_manager:device_type', args=[self.pk])


class Device(models.Model):
    name = models.CharField(max_length=64)
    serial_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    mac = models.CharField(max_length=100, unique=True, blank=True, null=True)

    device_type = models.ForeignKey(
        to='DeviceType',
        on_delete=models.CASCADE,
    )

    time_created = models.DateTimeField(auto_created=True, default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'devices'
        ordering = ('device_type', 'name')
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ip_manager:device', args=[self.pk])


class Subnet(models.Model):
    FAMILY_4 = 4
    FAMILY_6 = 6

    CHOICES = (
        (FAMILY_4, 'IPv4'),
        (FAMILY_6, 'IPv6'),
    )

    family = models.PositiveSmallIntegerField(
        choices=CHOICES,
    )

    name = models.CharField(max_length=100, blank=True, db_index=True)

    subnet = models.CharField(
        max_length=250,
        db_index=True,
        verbose_name="Subnet",
        unique=True,
        help_text='Subnet in CIDR notation, eg: "10.0.0.0/24" for IPv4 and "fdb6:21b:a477::9f7/64" for IPv6')

    broadcast_address = models.GenericIPAddressField(verbose_name="Broadcast IP")
    hostmask = models.GenericIPAddressField(verbose_name="Host Mask")
    netmask = models.GenericIPAddressField(verbose_name="Net Mask")

    total_hosts = models.BigIntegerField(verbose_name="Total IPs")
    reserved_hosts = models.BigIntegerField(verbose_name="Reserved IPs", default=2)
    utilization_percentage = models.TextField(verbose_name="Usage (%)", blank=True, null=True)

    description = models.CharField(max_length=100, blank=True)

    master_subnet = models.ForeignKey('self', on_delete=models.CASCADE,
                                      blank=True, null=True,
                                      related_name='child_subnet_set')

    vlan = models.ForeignKey(
        to='VLAN',
        on_delete=models.SET_NULL,
        related_name='vlans',
        blank=True,
        null=True
    )

    time_created = models.DateTimeField(auto_created=True, default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'subnets'
        verbose_name = 'Subnet'
        verbose_name_plural = 'Subnets'
        indexes = [
            models.Index(fields=['subnet'], name='subnet_idx')
        ]

    def __str__(self):
        if self.name:
            return '{0} {1}'.format(self.name, str(self.subnet))
        else:
            return str(self.subnet)

    def get_absolute_url(self):
        return reverse('ip_manager:subnet', args=[self.pk])

    def hosts(self):
        ip_list = list(ipaddress.ip_network(self.subnet).hosts())
        return ip_list

    def save(self, *args, **kwargs):

        self.family = ipaddress.ip_network(self.subnet).version

        self.broadcast_address = str(ipaddress.ip_network(self.subnet).broadcast_address)

        self.hostmask = str(ipaddress.ip_network(self.subnet).hostmask)
        self.netmask = str(ipaddress.ip_network(self.subnet).netmask)

        self.total_hosts = len(list(ipaddress.ip_network(self.subnet).hosts()))

        super().save(*args, **kwargs)


class IPAddress(models.Model):
    subnet = models.ForeignKey(
        to='Subnet',
        on_delete=models.PROTECT,
        related_name='ip_addresses',
        blank=True,
        null=True,
        verbose_name='Subnet'
    )

    address = models.GenericIPAddressField(
        verbose_name='IP',
        help_text='IP address'
    )

    STATUS_ACTIVE = 'active'
    STATUS_RESERVED = 'reserved'
    STATUS_DEPRECATED = 'deprecated'
    STATUS_DHCP = 'dhcp'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_RESERVED, 'Reserved'),
        (STATUS_DEPRECATED, 'Deprecated'),
        (STATUS_DHCP, 'DHCP'),
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='active',
        help_text='The operational status of this IP'
    )

    ROLE_LOOPBACK = 'loopback'
    ROLE_SECONDARY = 'secondary'
    ROLE_ANYCAST = 'anycast'
    ROLE_VIP = 'vip'
    ROLE_VRRP = 'vrrp'
    ROLE_HSRP = 'hsrp'
    ROLE_GLBP = 'glbp'
    ROLE_CARP = 'carp'

    IPAddressRoleChoices = (
        (ROLE_LOOPBACK, 'Loopback'),
        (ROLE_SECONDARY, 'Secondary'),
        (ROLE_ANYCAST, 'Anycast'),
        (ROLE_VIP, 'VIP'),
        (ROLE_VRRP, 'VRRP'),
        (ROLE_HSRP, 'HSRP'),
        (ROLE_GLBP, 'GLBP'),
        (ROLE_CARP, 'CARP'),
    )

    role = models.CharField(
        max_length=45,
        choices=IPAddressRoleChoices,
        blank=True,
        help_text='The functional role of this IP'
    )

    device = models.ForeignKey(
        to='Device',
        on_delete=models.CASCADE,
        related_name='ip_addresses',
        blank=True,
        null=True
    )

    nat_inside = models.OneToOneField(
        to='self',
        on_delete=models.SET_NULL,
        related_name='nat_outside',
        blank=True,
        null=True,
        verbose_name='NAT (Inside)',
        help_text='The IP for which this address is the "outside" IP'
    )

    dns_name = models.CharField(
        max_length=255,
        blank=True,
        validators=[DNSValidator],
        verbose_name='DNS Name',
        help_text='Hostname or FQDN (not case-sensitive)'
    )

    description = models.CharField(
        max_length=100,
        blank=True
    )

    time_created = models.DateTimeField(auto_created=True, default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'ips'
        ordering = ('address', 'pk')
        unique_together = ('address', 'subnet')
        verbose_name = 'IP'
        verbose_name_plural = 'IPs'

    def __str__(self):
        return str(self.address)

    def get_absolute_url(self):
        return reverse('ip_manager:ipaddress', args=[self.pk])

    def save(self, *args, **kwargs):
        # Force dns_name to lowercase
        self.dns_name = self.dns_name.lower()
        ##############################################################################

        sub = self.subnet
        reserved_hosts = sub.reserved_hosts
        sub.reserved_hosts = reserved_hosts + 1
        sub.save()

        reserved_hosts_num = sub.reserved_hosts
        total_host = sub.total_hosts

        sub.utilization_percentage = (reserved_hosts_num / total_host) * 100
        sub.save()

        super().save(*args, **kwargs)


class VLAN(models.Model):
    name = models.CharField(
        max_length=64
    )

    location = models.ForeignKey(
        to='Location',
        on_delete=models.PROTECT,
        related_name='vlans',
        blank=True,
        null=True
    )

    vid = models.PositiveSmallIntegerField(
        unique=True,
        verbose_name='ID',
        validators=[MinValueValidator(VLAN_VID_MIN), MaxValueValidator(VLAN_VID_MAX)]
    )

    STATUS_ACTIVE = 'active'
    STATUS_RESERVED = 'reserved'
    STATUS_DEPRECATED = 'deprecated'

    CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_RESERVED, 'Reserved'),
        (STATUS_DEPRECATED, 'Deprecated'),
    )

    status = models.CharField(
        max_length=50,
        choices=CHOICES,
        default='active'
    )

    description = models.CharField(
        max_length=100,
        blank=True
    )

    time_created = models.DateTimeField(auto_created=True, default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'vlans'
        ordering = ('vid', 'pk')

        verbose_name = 'VLAN'
        verbose_name_plural = 'VLANs'

    def __str__(self):
        return str(self.vid)

    def get_absolute_url(self):
        return reverse('ip_manager:vlan', args=[self.pk])


class Service(models.Model):
    name = models.CharField(
        max_length=30
    )

    PROTOCOL_TCP = 'TCP'
    PROTOCOL_UDP = 'UDP'

    CHOICES = (
        (PROTOCOL_TCP, 'TCP'),
        (PROTOCOL_UDP, 'UDP'),
    )

    protocol = models.CharField(
        max_length=20,
        choices=CHOICES
    )

    port = models.PositiveIntegerField(
        validators=[MinValueValidator(SERVICE_PORT_MIN), MaxValueValidator(SERVICE_PORT_MAX)],
        verbose_name='Port number'
    )

    ip_addresses = models.ManyToManyField(
        to='IPAddress',
        related_name='services',
        blank=True,
        verbose_name='IP addresses'
    )

    description = models.CharField(
        max_length=100,
        blank=True
    )

    time_created = models.DateTimeField(auto_created=True, default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'services'
        ordering = ('protocol', 'port', 'pk')
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return '{} ({}/{})'.format(self.name, self.port, self.protocol)

    def get_absolute_url(self):
        return reverse('ip_manager:service', args=[self.pk])
