from django.db import models
from users.models import User

class Studio(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['studio', 'start_time'],
                name='unique_studio_booking'
            )
        ]

# Create your models here.
