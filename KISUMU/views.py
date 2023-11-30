from django.shortcuts import render
from .models import Services,Blog,Comment,ContactUs,Products,Team,Testmonial,OurLocation



def home(request):
    services = Services.objects.all()[:5]
    products = Products.objects.all().order_by('?')
    testimonials = Testmonial.objects.all()
    team = Team.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    context = {
        'nav': 'home',
        'products' : products,
        'testimonials' : testimonials,
        'teams' : team,
        'blogs' : blogs,
        'services': services,
    }
    return render(request,'index.html',  context)


def product(request):
    return render(request, 'product.html', {'nav': 'product'})

def about(request):
    return render(request, 'about.html', {'nav': 'about'})


def services(request):
    services = Services.objects.all().order_by('?')
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
