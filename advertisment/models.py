from django.db import models

# Create your models here.


class AdvertisModel(models.Model):
    title = models.CharField(max_length=100, default="empty")
    link = models.CharField(max_length=250, default="#")
    image = models.ImageField(upload_to="images", default="default.jpg")

    def __str__(self):
        return self.title
    
