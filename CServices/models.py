from django.db import models


METHODS = (
    ('ROOM', 'room'),
    ('PHONE', 'phone'),
    ('ONLINE', 'online'),
    ('FOCUS', 'focus'),
    ('MIXED', 'mixed'),
)


class BidRequest(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=30)
    bid = models.FloatField(null=True)
    length = models.IntegerField()
    IR = models.IntegerField(null=True)
    method = models.CharField(max_length=10, choices=METHODS)


class WipRequest(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=30)
    bid = models.FloatField(null=True)
    length = models.IntegerField()
    IR = models.IntegerField(null=True)
    cost = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    method = models.CharField(max_length=10, choices=METHODS)

