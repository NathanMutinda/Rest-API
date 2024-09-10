from django.db import models

# Create your models here.
# this is a test line code


class Stocks(models.Model):
    Amazon = models.CharField(max_length=100)
    Facebook = models.CharField(max_length=100)

    def __str__(self):
        return self.Amazon

