from django.db import models
from django.conf import settings

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Cars(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")

    model = models.CharField(max_length=100)
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=50, choices=[
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid')
    ])
    quantity = models.PositiveIntegerField(default=0)
    mileage = models.PositiveIntegerField()
    img = models.ImageField(upload_to='cars/', null=True, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"

class Comment(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cuser", null=True)
    content = models.TextField()

    def __str__(self):
        return f"Commented by {self.id}"

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ruser", null=True)
    content = models.TextField()

    def __str__(self):
        return f"Replied by{self.id}"