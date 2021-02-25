from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index  , name='index'),
    url(r'contacted$', views.contacted  , name='contacted'),
    url(r'product/(?P<id>\d+)$', views.productDetail  , name='productDetail'),
    url(r'audit/(?P<id>\d+)$', views.auditDetail  , name='audit'),
    url(r'consulting/(?P<id>\d+)$', views.consultingDetail  , name='consulting'),
    url(r'security/(?P<id>\d+)$', views.securityDetail  , name='security'),
    url(r'solution/(?P<id>\d+)$', views.solutionDetail  , name='solution'),
    url(r'services$', views.services  , name='services'),
    url(r'products$', views.products  , name='products'),
    url(r'team$', views.team  , name='team'),
    url(r'packagedetail/(?P<id>\d+)$', views.packagedetail  , name='packagedetail'),
    url(r'nafilinux$', views.nafilinux  , name='nafilinux'),
    url(r'auditservice$', views.auditservice  , name='auditservice'),
   url(r'auditrevolution$', views.auditrevolution  , name='auditrevolution'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)