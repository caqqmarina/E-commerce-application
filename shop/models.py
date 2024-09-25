from django.db import models
import uuid
from django.contrib.auth.models import User

SLIME_QUALITY_CHOICES = [
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Fair', 'Fair'),
    ('Poor', 'Poor'),
]

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()  
    description = models.TextField()
    slime_quality = models.CharField(max_length=50, choices=SLIME_QUALITY_CHOICES, default='Excellent')

    def __str__(self):
        return self.name

# name: CharField
# age: IntegerField
# is_happy: BooleanField

# class Person(models.Model):
#     name = models.CharField(max_length=80)
#     age = models.IntegerField()
#     is_happy = models.BooleanField()