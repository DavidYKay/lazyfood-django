from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    restaurant_code = models.IntegerField()

    def __unicode__(self):
      return self.name

class Tray(models.Model):
    """
    Represents an order to be made at a given restaurant.
    """
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)

    class Meta:
      pass

    def __unicode__(self):
      return self.name

class TrayItem(models.Model):
    tray = models.ForeignKey(Tray)
    name = models.CharField(max_length=60)
    quantity = models.IntegerField()
    item_code = models.IntegerField()

    def __unicode__(self):
      return self.name

class Option(models.Model):
    tray_item = models.ForeignKey(TrayItem)
    option_code = models.IntegerField()
    name = models.CharField(max_length=60)

    def __unicode__(self):
      return "%s: Option %d - %s" % (self.tray_item, self.option_code, self.name)
