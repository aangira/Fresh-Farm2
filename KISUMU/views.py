

from django.shortcuts import render
def home(request):
    return render(request,'home.html',  {'bike': 'home'})


def viewdata(request):
    return render(request, 'team.html', {'bike': 'team'})




# Create your views here.
