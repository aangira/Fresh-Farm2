from django.shortcuts import render



def home(request):
    return render(request,'index.html',  {'bike': 'home'})


def product(request):
    return render(request, 'product.html', {'nav': 'product'})

def about(request):
    return render(request, 'about.html', {'nav': 'about'})


def services(request):
    return render(request, 'service.html', {'nav': 'service'})


def team(request):
    return render(request, 'team.html', {'nav': 'team'})


def contact(request):
    return render(request, 'contact.html', {'nav': 'contact'})


def viewdata(request):
    return render(request, 'team.html', {'nav': 'team'})


def viewdata(request):
    return render(request, 'team.html', {'nav': 'team'})


def viewdata(request):
    return render(request, 'team.html', {'nav': 'team'})




# Create your views here.
