from django.shortcuts import render
from .models import Service

# Create your views here.
def home(request):
    return render(request,'home.html',{})


def services(request):
    services = Service.objects.all()
    return render(request,'services.html',{'services' : services})



def services_detail(request, pk):
    service = Service.objects.get(id = pk)

    context = {'service': service}
    return render(request,'services-detail.html', context)

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})