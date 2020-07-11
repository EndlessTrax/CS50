from django.db import models

from .locations import LOCATION_CHOICES


# Tree Model
class Tree(models.Model):
    name = models.CharField(max_length=80)
    species = models.CharField(max_length=80) # drop max_length when drop down form complete
    description = models.TextField()
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='trees/')
    sold = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        ordering = ['-created']
