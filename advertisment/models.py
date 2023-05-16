from django.db import models


class AdvertisModel(models.Model):
    title = models.CharField(max_length=100,default = 'empty' )
    image = models.ImageField(upload_to='adv/',default = "default.jpg")
    link = models.CharField(max_length=255,default='#')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']
        
    