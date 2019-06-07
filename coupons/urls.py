from django.conf.urls import url
from . import views

app_name = 'coupons'

urlpatterns = [
    url(r'^apply/$', views.coupon_apply, name='apply'),
    url(r'^remove/$', views.coupon_remove, name='remove'),
]
