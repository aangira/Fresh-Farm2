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


def blog(request):
    return render(request, 'blog.html', {'nav': 'blog'})


def details(request):
    return render(request, 'detail.html', {'nav': 'detail'})


def features(request):
    return render(request, 'feature.html', {'nav': 'feature'})


def testimonials(request):
    return render(request, 'testimonial.html', {'nav': 'testimonial'})




# Create your views here.
