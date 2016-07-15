from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory

from .forms import cs_wip_req_form, BidReqForm, BidOptionForm
from CServices.models import WipRequest, BidRequest


def cs_home(request):
    wip_requests = WipRequest.objects.all()
    headers = ['Author', 'P#', 'Name', 'Size', 'Bid', 'Length', 'IR', 'Cost', 'Start', 'End', 'Method']
    bid_requests = BidRequest.objects.all()
    bl_headers = ['ID', 'P#','Name']
    return render(request, 'CServices/cs_home.html', {"headers": headers,
                                                      "wips": wip_requests,
                                                      "bl_headers": bl_headers,
                                                      "bids": bid_requests})


def wip_req(request):
    if request.method == 'POST':
        form = cs_wip_req_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = cs_wip_req_form()

    return render(request, 'CServices/cs_wip_req.html', {'form': form})


def bid_req(request):
    BidReqFormSet = formset_factory(BidOptionForm, extra=5)
    if request.method == "POST":
        bidreq = BidReqForm(request.POST)
        formset = BidReqFormSet(request.POST)
        if bidreq.is_valid():

            bidreq.save()
        if formset.is_valid():
            for form in formset:
                post = form.save(commit=False)
                this_bid = BidRequest.objects.get(p_num=request.POST['p_num'])
                post.bidreqticket = this_bid
                post.save()


        else:
            return render(request, 'CServices/cs_bid_req.html', {'formset': formset,
                                                                 'bidreq': bidreq})
        return HttpResponseRedirect('/')
    else:
        bidreq = BidReqForm()
        return render(request, 'CServices/cs_bid_req.html', {'formset': BidReqFormSet,
                                                             'bidreq': bidreq})



def bid_req_rev(request):
    form = dir(request)
    return render(request, 'CServices/cs_bid_req_review.html', {'form': form})


def bid_builder(request):
    return render(request, 'CServices/cs_bid_builder.html', {})