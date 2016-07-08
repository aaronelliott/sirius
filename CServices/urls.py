from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cs_home, name='cs_home'),
    url(r'^wip_req/$', views.wip_req, name='wip_req'),
    url(r'^bid_req/$', views.bid_req, name='bid-req'),
    url(r'^bid_builder/$', views.bid_builder, name='bid-builder'),

]