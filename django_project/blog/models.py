from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tasks(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    Name = models.CharField(max_length=100)
    Content = models.CharField(max_length=200)
    CreatedDate = models.CharField(max_length=100)
    Pickup = models.CharField(max_length=100)
    Picture = models.ImageField(upload_to='task_pictures/', blank=True, null=True)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('Task-Detail', kwargs={'pk': self.pk})
