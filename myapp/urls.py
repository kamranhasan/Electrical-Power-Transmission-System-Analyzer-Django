from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index  , name='index'),
    url(r'contacted$', views.contacted  , name='contacted'),
    url(r'product/(?P<id>\d+)$', views.productDetail  , name='productDetail'),
    url(r'service/(?P<id>\d+)$', views.serviceDetail  , name='serviceDetail'),
    url(r'services$', views.services  , name='services'),
    url(r'products$', views.products  , name='products'),
    url(r'team$', views.team  , name='team'),
    url(r'packagedetail/(?P<id>\d+)$', views.packagedetail  , name='packagedetail'),
    url(r'nafilinux$', views.nafilinux  , name='nafilinux'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)