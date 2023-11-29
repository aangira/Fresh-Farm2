from django.db import models

class Services(models.Model):
    service = models.CharField(max_length=50)
    desc = models.TextField()
    icon = models.CharField(max_length=30)
    
    def __str__(self):
        return self.service
    
    
class Products(models.Models):
    name = models.CharField( max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs')
    date_posted = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.title[:10]
    
    
class Comment(models.Model):
    user_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField()
    date_posted = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.user_name
    
    
class Team(models.Model):
    farmer_name = models.CharField(max_length=100)
    desgination = models.CharField( max_length=500)
    image = models.ImageField(upload_to='teams')
    
    def __str__(self):
        return self.farmer_name
    
    
class Testmonial(models.Model):
    client_name = models.CharField( max_length=100)
    image = models.ImageField(upload_to='client')
    desc = models.TextField()
    
    def __str__(self):
        return self.client_name
    
    
class ContactUs(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    subject = models.TextField()
    message = models.TextField()
    
    def __str__(self):
        return self.name


class OurLocation(models.Model):
    title = models.CharField( max_length=50)
    ways = models.CharField( max_length=50)
    icon = models.CharField( max_length=30)
    
    def __str__(self):
        return self.title

# Create your models here.
