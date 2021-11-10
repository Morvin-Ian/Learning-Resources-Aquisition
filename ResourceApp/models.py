from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Resource(models.Model):
    res_title = models.CharField(max_length=50)
    res_author =models.CharField(max_length=50)
    res_copies = models.IntegerField(default=5)
   

    def __str__(self):
        return self.res_title

class Borrowed_Resource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed = models.ForeignKey(Resource, on_delete=models.CASCADE)

    borrowed_date = datetime.datetime.now()
    recorded_borrowing_date = models.DateTimeField(auto_now_add=True)
    
    period = datetime.timedelta(days=30)
    returning_date = borrowed_date+period
    recorded_returning_date = models.DateTimeField(default=returning_date)

    def __str__(self):
        return f"{self.user.username}-{self.borrowed}"



