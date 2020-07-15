from django.contrib.auth.models import AbstractUser



class CustomUer(AbstractUser):
    group=models.ManyToManyField('core.Group')

class Group(models.Model):


# Register your models here.
