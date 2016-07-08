from django import forms
from .models import WipRequest, BidRequest

METHODS = (
    ('ROOM', 'room'),
    ('PHONE', 'phone'),
    ('ONLINE', 'online'),
    ('FOCUS', 'focus'),
    ('MIXED', 'mixed'),
)


class cs_bid_req_form(forms.ModelForm):

    class Meta:
        model = BidRequest
        fields = (
            'name', 'bid', 'length', 'IR', 'method',
        )


class cs_wip_req_form(forms.ModelForm):

    class Meta:
        model = WipRequest
        fields = (
            'name', 'bid', 'length', 'IR', 'cost', 'start', 'end', 'method'
        )
