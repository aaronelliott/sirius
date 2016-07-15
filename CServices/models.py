from django.db import models


METHODS = (
    ('ROOM', 'room'),
    ('PHONE', 'phone'),
    ('ONLINE', 'online'),
    ('FOCUS', 'focus'),
    ('MIXED', 'mixed'),
)

STATES = (
    ('PENDING', 'pending'),
    ('ACTIVE', 'active'),
    ('COMPLETE', 'complete')
)


class BidRequest(models.Model):
    name = models.CharField(max_length=30)
    p_num = models.IntegerField(unique=True)


class BidOption(models.Model):
    bidreqticket = models.ForeignKey(BidRequest)
    option = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    length = models.IntegerField(null=True)
    bid = models.FloatField(null=True)
    IR = models.IntegerField(null=True)
    method = models.CharField(max_length=10, choices=METHODS, null=True)


class WipRequest(models.Model):
    author = models.ForeignKey('auth.User')
    p_num = models.CharField(max_length=7)
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    bid = models.FloatField(null=True)
    length = models.IntegerField()
    IR = models.IntegerField(null=True)
    cost = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    method = models.CharField(max_length=10, choices=METHODS)

