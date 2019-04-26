from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
