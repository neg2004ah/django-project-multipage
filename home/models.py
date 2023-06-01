from django.db import models

class CheapPackages(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    
    
    def __str__(self) :
        return self.city
    
    
class LuxuryPackages(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    
    
    def __str__(self) :
        return self.city

class CampingPackages(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    
    
    def __str__(self) :
        return self.city  
    

class Newsletter(models.Model):
    email =  models.EmailField()
    
    def __str__(self):
        return self.email
    
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.name

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    