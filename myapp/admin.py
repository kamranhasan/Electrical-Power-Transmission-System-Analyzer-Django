from django.contrib import admin
from .models import Service,Product,Testimonial,Team,Contact,Packages,Audit_Service,IS_Consultancy_Service,IS_Security_Service,Software_Solutions_Service
# Register your models here.
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Testimonial)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Packages)
admin.site.register(Audit_Service)
admin.site.register(IS_Security_Service)
admin.site.register(IS_Consultancy_Service)
admin.site.register(Software_Solutions_Service)