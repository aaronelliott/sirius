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
    p_num = models.IntegerField()


class BidOption(models.Model):
    bidreq = models.ForeignKey(BidRequest)
    option = models.IntegerField()
    size = models.IntegerField()
    length = models.IntegerField()
    bid = models.FloatField()
    IR = models.IntegerField()
    method = models.CharField(max_length=10, choices=METHODS)


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

