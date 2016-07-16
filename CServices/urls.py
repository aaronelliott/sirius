from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cs_home, name='cs_home'),
    url(r'^wip_req/$', views.wip_req, name='wip_req'),
    url(r'^bid_req/$', views.bid_req, name='bid-req'),
    url(r'^bid_builder/$', views.bid_builder, name='bid-builder'),
    url(r'^bid_req_rev/$', views.bid_req_rev, name='bid-req-rev'),
    url(r'^bid_detail/(?P<p_num>[0-9]{6})/$', views.bid_detail, name='bid-detail'),

]