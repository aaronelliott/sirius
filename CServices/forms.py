from django import forms
from .models import WipRequest, BidRequest, BidOption

METHODS = (
    ('ROOM', 'room'),
    ('PHONE', 'phone'),
    ('ONLINE', 'online'),
    ('FOCUS', 'focus'),
    ('MIXED', 'mixed'),
)


class BidReqForm(forms.ModelForm):
    class Meta:
        model = BidRequest
        fields = (
            'name', 'p_num',
        )


class BidOptionForm(forms.ModelForm):
    class Meta:
        model = BidOption
        fields = (
            'size', 'length', 'bid', 'IR', 'method',
        )
        exclude = (
            'bidreqticket', 'option',
        )


class cs_wip_req_form(forms.ModelForm):

    class Meta:
        model = WipRequest
        fields = (
            'p_num', 'name', 'size','bid', 'length', 'IR', 'cost', 'start', 'end', 'method',
        )
