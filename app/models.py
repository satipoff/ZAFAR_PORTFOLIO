from django.db import models

class aloqa(models.Model):
    telefon = models.IntegerField()
    online_yozish = models.CharField(max_length=500)
    instagram = models.URLField(max_length=200)
    whatsapp = models.URLField(max_length=200)

    def __str__(self):
        return self.telefon
    
# class portfolio(models.Model):
#     logo_branding = 