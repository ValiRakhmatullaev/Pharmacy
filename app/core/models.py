# Клиент выбирает необходимый препарат из списка доступных.
# Заполнять форму заказа, указывая количество и дозировку.
# Клиент оплачивает заказ. Фармацевт управляет списком препаратов.
# Часть  препаратов требуют электронного рецепта, которые можно значит клиенту только врач.
# Клиент может сделать запрос врачу на продление рецепта


from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from address.models import AddressField
from djmoney.models.fields import MoneyField
from django.db import models


class Client(AbstractUser):
    addresses = models.ManyToManyField("core.ClientAddress", on_delete=models.CASCADE, related_name='client')
    recipe = models.ForeignKey('core.Doc', on_delete=models.CASCADE, related_name='client')


class Pharmacist(models.Model):
    # status = models.BigAutoField(defoult=False)
    # pills = models.ManyToManyField(get_user_model(), on_delete=models.CASCADE, related_name='pharmacies')
    # address = AddressField()
    list = models.ForeignKey('core.Medecine', on_delete=models.CASCADE, related_name='pharmacist')


class Medecine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = MoneyField(max_digits=7, decimal_placec=2, default_currency='USD')


class Doc(models.Model):
    type = models.ForeignKey('core.Type', on_delete=models.CASCADE, related_name='doctors')


class Recipe(models.Model):
    recipe
    to
    client
    recipe
    to
    doctor


class Type(models.Model):
    type_name = models.CharField(max_length=50)


class ClientAddress(models.Model):
    address = AddressField()


class Order(models.Model):
    BY_CARD = 'BY CARD'
    BY_CASH = 'BY CASH'
    PAYMENT_METHOD = (
        (1, BY_CARD),
        (2, BY_CASH),
    )
    status
    client = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='order')
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD)
    quantity = models.PositiveIntegerField()


class DrugForm(models.Model):
    title = models.CharField()


class Drug(models.Model):
    name = models.CharField(max_length=50)
    price = MoneyField(max_digits=7, decimal_places=2, default_currency='USD')
    effect = models.TextField()
    overdose = models.TextField()
    drug_form=
