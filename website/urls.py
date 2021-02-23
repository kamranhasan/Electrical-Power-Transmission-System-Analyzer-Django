"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings


from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin


from myapp.models import *

class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

# Register your models here.
admin_site.register(Service)
admin_site.register(Product)
admin_site.register(Testimonial)
admin_site.register(Team)
admin_site.register(Contact)
admin_site.register(Packages)
admin_site.register(Audit_Service)
admin_site.register(IS_Security_Service)
admin_site.register(IS_Consultancy_Service)
admin_site.register(Software_Solutions_Service)




urlpatterns = [
    path('priadmin/', admin_site.urls),
    path('', include("myapp.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
