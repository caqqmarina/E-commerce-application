from django.db import models
import uuid

SLIME_QUALITY_CHOICES = [
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Fair', 'Fair'),
    ('Poor', 'Poor'),
]

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()  
    description = models.TextField()
    slime_quality = models.CharField(max_length=50, choices=SLIME_QUALITY_CHOICES, default='Excellent')

    def __str__(self):
        return self.name
    