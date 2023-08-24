from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):   
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Voetbalspeler(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    naam_voetballer = models.CharField(max_length=100)
    actuele_voetbalclub = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    laatste_wijziging_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.naam_voetballer
