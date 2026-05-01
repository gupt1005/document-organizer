from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)
    renewal_date = models.DateField(null=True, blank=True, db_index=True)
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            # filtering reports
            models.Index(fields=['user', 'category']),
            #"expiring soon" queries  
            models.Index(fields=['renewal_date']),      
        ]
    

'''
class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    renewal_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
'''
