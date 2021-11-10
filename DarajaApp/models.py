from django.db import models
from django.contrib.auth.models import User


class TransactionDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username

