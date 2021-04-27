from django.db import models
from django.urls import reverse 


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    post_author = models.ForeignKey('auth.User',on_delete=(models.CASCADE))



    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "...."
    
    def get_absolute_url(self): # new 
        return reverse('post_detail', args=[str(self.id)])

        