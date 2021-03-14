from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    wealth_type = models.CharField(max_length=100)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name            