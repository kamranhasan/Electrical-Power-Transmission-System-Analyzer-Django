from django.shortcuts import render
from .models import *
from .forms import Messages
# Create your views here.
def index(request):
    service = Service.objects.all()
    product = Product.objects.all()
    testimonial = Testimonial.objects.all()
    team = Team.objects.all()[:4]
    contact = Messages()
    respond = 'Send Message'
    context = {
        'service' : service,
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
            return render(request,'index.html',{'respond':respond})
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'index.html',{'respond':respond})
    context = {
        'service' : service,
        'product' : product, 
        'testimonial' : testimonial,
        'team' : team,
        'respond' : respond
        }
    return render(request, 'index.html', context)
