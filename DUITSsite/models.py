from django.db import models

class Corse(models.Model):
    titel = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titel
    
class Material(models.Model):
    corse = models.ForeignKey(Corse, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='corse_materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.corse})"