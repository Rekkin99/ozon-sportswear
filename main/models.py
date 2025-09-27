import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('jersey', 'Jersey'),
        ('ball', 'Ball'),
        ('bottle', 'Bottle'),
        ('accessory', 'Accessory'),
    ]
    
    # Atribut
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(default='footwear', choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    
    # Return Products Name
    def __str__(self):
        return self.name