from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    img = models.ImageField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


