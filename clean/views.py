from django.shortcuts import render,redirect
from .models import Service
from .forms import RequestForm

# Create your views here.
def home(request):
    services = Service.objects.all()
    return render(request,'home.html',{'services': services})


def services(request):
    services = Service.objects.all()
    
    return render(request,'services.html',{'services' : services})



def services_detail(request, pk):
    service = Service.objects.get(id = pk)

    context = {'service': service}
    return render(request,'services-detail.html', context)

def about(request):
    return render(request,'about.html',{})

# def contact(request):
#     return render(request,'contact.html',{})

def contact(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
         
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RequestForm()
        
    return render(request,'contact.html',{'form' : form})
            