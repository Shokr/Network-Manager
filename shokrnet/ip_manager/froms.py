from django import forms

from .models import *


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = '__all__'


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


class SubnetForm(forms.ModelForm):
    class Meta:
        model = Subnet
        fields = '__all__'


class IPForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = '__all__'


class VLANForm(forms.ModelForm):
    class Meta:
        model = VLAN
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
