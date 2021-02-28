from django.shortcuts import render
from .models import *
from .forms import Messages
# Create your views here.
def index(request):
    service3 = IS_Security_Service.objects.all()
    service4 = Software_Solutions_Service.objects.all()
    product = Product.objects.all()[:4]
    testimonial = Testimonial.objects.all()
    team = Team.objects.all().order_by('id')[:3]
    contact = Messages()
    respond = 'Send Message'
    context = {
        'service3' : service3,
        'service4' : service4,
        'product' : product, 
        'testimonial' : testimonial,
        'team' : team,
        'contact' : contact,
        'respond' : respond
        }
    return render(request, 'index.html', context)

def contacted(request):
    service = Service.objects.all()
    product = Product.objects.all()
    testimonial = Testimonial.objects.all()
    team = Team.objects.all()[:4]
    if request.method=="POST":
        data=Messages(request.POST)
        if data.is_valid():
            data.save()
            respond='Your Message has been sent successfully!'
            return render(request,'index.html',{'respond':respond,'product':product,'service':service,'team':team})
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'index.html',{'respond':respond ,'product':product,'service':service,'team':team})
    respond='Send Message'
    context = {
        'service' : service,
        'product' : product, 
        'testimonial' : testimonial,
        'team' : team,
        'respond' : respond
        }
    return render(request, 'index.html', context)


def productDetail(request,id):
    product=Product.objects.get(id=id)
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'productdetail.html',{'product': product,
                                                'contact' : contact,
                                                'respond' : respond
                                                }
                )


def auditDetail(request,id):
    service=Audit_Service.objects.get(id=id)
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'servicedetail.html',{'service': service,
                                                'contact' : contact,
                                                'respond' : respond
                                                }
                )

def consultingDetail(request,id):
    service=IS_Consultancy_Service.objects.get(id=id)
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'servicedetail.html',{'service': service,
                                                'contact' : contact,
                                                'respond' : respond
                                                }
                )


def securityDetail(request,id):
    service=IS_Security_Service.objects.get(id=id)
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'servicedetail.html',{'service': service,
                                                'contact' : contact,
                                                'respond' : respond
                                                }
                )


def solutionDetail(request,id):
    service=Software_Solutions_Service.objects.get(id=id)
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'servicedetail.html',{'service': service,
                                                'contact' : contact,
                                                'respond' : respond
                                                }
                )


def services(request):
    service1 = Audit_Service.objects.all()
    service2 = IS_Consultancy_Service.objects.all()
    service3 = IS_Security_Service.objects.all()
    service4 = Software_Solutions_Service.objects.all()
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'services.html',{'service1': service1,
                                            'service2': service2,
                                            'service3': service3,
                                            'service4': service4,
                                            'contact' : contact,
                                            'respond' : respond
                                            }
                )


def products(request):
    product=Product.objects.all()
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'products.html',{'product': product,
                                                'contact' : contact,
                                                'respond' : respond
                                            }
                )

def team(request):
    team=Team.objects.all().order_by('id')
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'team.html',{'team': team,
                                                'contact' : contact,
                                                'respond' : respond
                                        }
                )

def packagedetail(request,id):
    package=Packages.objects.get(id=id)
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'packagedetail.html',{'package': package,
                                                'contact' : contact,
                                                'respond' : respond
                                                }
                )


def nafilinux(request):
    Information_gathering=Packages.objects.filter(domain_name='Information Gathering')
    Vulnerability_Analysis=Packages.objects.filter(domain_name='Vulnerability Analysis')
    Wireless_Attacks=Packages.objects.filter(domain_name='Wireless Attacks')
    Web_Applications=Packages.objects.filter(domain_name='Web Applications')
    Exploitation_Tools=Packages.objects.filter(domain_name='Exploitation Tools')
    Stress_Testing=Packages.objects.filter(domain_name='Stress Testing')
    Forensics_Tools=Packages.objects.filter(domain_name='Forensics Tools')
    Sniffing_Spoofing=Packages.objects.filter(domain_name='Sniffing & Spoofing')
    Password_Attacks=Packages.objects.filter(domain_name='Password Attacks')
    Maintaining_Access=Packages.objects.filter(domain_name='Maintaining Access')
    Reverse_Engineering=Packages.objects.filter(domain_name='Reverse Engineering')
    Reporting_Tools=Packages.objects.filter(domain_name='Reporting Tools')
    Hardware_Hacking=Packages.objects.filter(domain_name='Hardware Hacking')

    contact = Messages()
    respond = 'Send Message'
    context = {'Information_gathering' : Information_gathering,
                'Vulnerability_Analysis' : Vulnerability_Analysis,
                'Wireless_Attacks' : Wireless_Attacks,
                'Web_Applications' : Web_Applications,
                'Exploitation_Tools' : Exploitation_Tools,
                'Stress_Testing' : Stress_Testing,
                'Forensics_Tools' : Forensics_Tools,
                'Sniffing_Spoofing' : Sniffing_Spoofing,
                'Password_Attacks' : Password_Attacks,
                'Maintaining_Access' : Maintaining_Access,
                'Reverse_Engineering' : Reverse_Engineering,
                'Reporting_Tools' : Reporting_Tools,
                'Hardware_Hacking' : Hardware_Hacking,
                'contact' : contact,
                'respond' : respond,
                }
    return render(request, 'nafilinux.html',context )



def auditservice(request):
    service = Audit_Service.objects.all()
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'auditservice.html',{'service': service,'contact' : contact,'respond' : respond})


def auditrevolution(request):
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'auditrevolution.html',{'contact' : contact,'respond' : respond})


def consultingservice(request):
    service = IS_Consultancy_Service.objects.all()
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'consultingservice.html',{'service': service,'contact' : contact,'respond' : respond, })


def digitaltransformation(request):
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'digitaltransformation.html',{'contact' : contact,'respond' : respond})

def riskservice(request):
    service = IS_Security_Service.objects.all()
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'riskservice.html',{'service': service,'contact' : contact,'respond' : respond})

def softwareservice(request):
    service = Software_Solutions_Service.objects.all()
    contact = Messages()
    respond = 'Send Message'
    return render(request, 'softwareservice.html',{'service': service,'contact' : contact,'respond' : respond})
