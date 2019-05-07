from django.db import models
from django.utils import dateformat
class Progadas(models.Model):
    date=models.DateField()
    customer_name=models.CharField(max_length=50)
    prodect_order=models.IntegerField()
    cus_amount=models.IntegerField()
    email=models.EmailField(max_length=60)
class ChooseFile(models.Model):
    choose_file=models.FileField(max_length=30)

