from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from address.models import AddressField
from django.db import models


class CustomUser(AbstractUser):
    pacients = models.ManyToManyField('core.')


class Pharmacy(models.Model):
    status = models.BigAutoField(defoult=False)
    pills = models.ManyToManyField(get_user_model(), on_delete=models.CASCADE, related_name='Pharmacies')
    address = AddressField()


class Drug(models.Model):
    description = models.TextField(blank=True)
    cost = models.SmallIntegerField()


class Doc(models.Model):
    type = models.ForeignKey('core.Type', on_delete=models.CASCADE, related_name='Doctors')
    address = AddressField()


class Type(models.Model):
    type_name = models.CharField(max_length=50)
