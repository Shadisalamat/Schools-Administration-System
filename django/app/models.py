from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Statements(models.Model):
    name = models.CharField(max_length=50)
    amount_direction = models.SmallIntegerField(choices=((0, 'Income'), (1, 'Outlay')))
    exchange_rate = models.FloatField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)