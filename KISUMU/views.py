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
    team = Team.objects.all().order_by('?')
    context = {'nav': 'about','teams':team}
    return render(request, 'about.html', context)


def services(request):
    services = Services.objects.all().order_by('?')
    testimonials = Testmonial.objects.all()
    context = {'nav': 'service','services':services,'testimonials' : testimonials,}
    return render(request, 'service.html', context )


def team(request):
    return render(request, 'team.html', {'nav': 'team'})


def contact(request):
    location = OurLocation.objects.all()
    context = {'nav': 'contact','locations':location}
    return render(request, 'contact.html', context )


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'nav': 'blog',
        'blogs':blogs
    }
    return render(request, 'blog.html', context)


def details(request):
    return render(request, 'detail.html', {'nav': 'detail'})


def features(request):
    return render(request, 'feature.html', {'nav': 'feature'})


def testimonials(request):
    return render(request, 'testimonial.html', {'nav': 'testimonial'})




# Create your views here.
