# Generated by Django 3.0.4 on 2020-03-28 11:16
import django.core.validators
import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_created=True,
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "serial_number",
                    models.CharField(blank=True,
                                     max_length=100,
                                     null=True,
                                     unique=True),
                ),
                (
                    "mac",
                    models.CharField(blank=True,
                                     max_length=100,
                                     null=True,
                                     unique=True),
                ),
            ],
            options={
                "verbose_name": "Device",
                "verbose_name_plural": "Devices",
                "db_table": "devices",
                "ordering": ("device_type", "name"),
            },
        ),
        migrations.CreateModel(
            name="DeviceType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_created=True,
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                    ),
                ),
                (
                    "manufacturer",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "model_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("name", models.CharField(max_length=64)),
            ],
            options={
                "verbose_name": "Device Type",
                "verbose_name_plural": "Device Types",
                "db_table": "device_types",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="IPAddress",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_created=True,
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                    ),
                ),
                ("address",
                 models.GenericIPAddressField(help_text="IPv4 address")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("reserved", "Reserved"),
                            ("deprecated", "Deprecated"),
                            ("dhcp", "DHCP"),
                        ],
                        help_text="The operational status of this IP",
                        max_length=50,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("loopback", "Loopback"),
                            ("secondary", "Secondary"),
                            ("anycast", "Anycast"),
                            ("vip", "VIP"),
                            ("vrrp", "VRRP"),
                            ("hsrp", "HSRP"),
                            ("glbp", "GLBP"),
                            ("carp", "CARP"),
                        ],
                        help_text="The functional role of this IP",
                        max_length=45,
                    ),
                ),
                (
                    "dns_name",
                    models.CharField(
                        blank=True,
                        help_text="Hostname or FQDN (not case-sensitive)",
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid",
                                message=
                                "Only alphanumeric characters, hyphens, periods, and underscores are allowed in DNS names",
                                regex="^[0-9A-Za-z._-]+$",
                            )
                        ],
                        verbose_name="DNS Name",
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=100)),
                (
                    "device",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ip_addresses",
                        to="ip_manager.Device",
                    ),
                ),
                (
                    "nat_inside",
                    models.OneToOneField(
                        blank=True,
                        help_text=
                        'The IP for which this address is the "outside" IP',
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="nat_outside",
                        to="ip_manager.IPAddress",
                        verbose_name="NAT (Inside)",
                    ),
                ),
            ],
            options={
                "verbose_name": "IP",
                "verbose_name_plural": "IPs",
                "db_table": "ips",
                "ordering": ("address", "pk"),
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_created=True,
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50,
                                          null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "geolocation",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
            options={
                "verbose_name": "Network Location",
                "verbose_name_plural": "Network Locations",
                "db_table": "Locations",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="VLAN",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_created=True,
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "vid",
                    models.PositiveSmallIntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(4094),
                        ],
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("reserved", "Reserved"),
                            ("deprecated", "Deprecated"),
                        ],
                        default="active",
                        max_length=50,
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=100)),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="vlans",
                        to="ip_manager.Location",
                    ),
                ),
            ],
            options={
                "verbose_name": "VLAN",
                "verbose_name_plural": "VLANs",
                "db_table": "vlans",
                "ordering": ("vid", "pk"),
            },
        ),
        migrations.CreateModel(
            name="Subnet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_created=True,
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                    ),
                ),
                (
                    "family",
                    models.PositiveSmallIntegerField(choices=[(4, "IPv4"),
                                                              (6, "IPv6")],
                                                     editable=False),
                ),
                ("name",
                 models.CharField(blank=True, db_index=True, max_length=100)),
                (
                    "subnet",
                    models.CharField(
                        db_index=True,
                        help_text=
                        'Subnet in CIDR notation, eg: "10.0.0.0/24" for IPv4 and "fdb6:21b:a477::9f7/64" for IPv6',
                        max_length=250,
                        unique=True,
                        verbose_name="Subnet",
                    ),
                ),
                (
                    "broadcast_address",
                    models.GenericIPAddressField(verbose_name="Broadcast IP"),
                ),
                ("hostmask",
                 models.GenericIPAddressField(verbose_name="Host Mask")),
                ("netmask",
                 models.GenericIPAddressField(verbose_name="Net Mask")),
                ("total_hosts",
                 models.BigIntegerField(verbose_name="Total IPs")),
                (
                    "reserved_hosts",
                    models.BigIntegerField(default=2,
                                           verbose_name="Reserved IPs"),
                ),
                (
                    "utilization_percentage",
                    models.TextField(blank=True,
                                     null=True,
                                     verbose_name="Usage (%)"),
                ),
                ("description", models.CharField(blank=True, max_length=100)),
                (
                    "master_subnet",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child_subnet_set",
                        to="ip_manager.Subnet",
                    ),
                ),
                (
                    "vlan",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="vlans",
                        to="ip_manager.VLAN",
                    ),
                ),
            ],
            options={
                "verbose_name": "Subnet",
                "verbose_name_plural": "Subnets",
                "db_table": "subnets",
            },
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_created=True,
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "protocol",
                    models.CharField(choices=[("TCP", "TCP"), ("UDP", "UDP")],
                                     max_length=20),
                ),
                (
                    "port",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(65535),
                        ],
                        verbose_name="Port number",
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=100)),
                (
                    "ip_addresses",
                    models.ManyToManyField(
                        blank=True,
                        related_name="services",
                        to="ip_manager.IPAddress",
                        verbose_name="IP addresses",
                    ),
                ),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
                "db_table": "services",
                "ordering": ("protocol", "port", "pk"),
            },
        ),
        migrations.AddField(
            model_name="ipaddress",
            name="subnet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ip_addresses",
                to="ip_manager.Subnet",
                verbose_name="Subnet",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ip_manager.DeviceType"),
        ),
        migrations.AddIndex(
            model_name="subnet",
            index=models.Index(fields=["subnet"], name="subnet_idx"),
        ),
        migrations.AlterUniqueTogether(
            name="ipaddress",
            unique_together={("address", "subnet")},
        ),
    ]
