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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    