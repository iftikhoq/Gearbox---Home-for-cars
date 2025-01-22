from django.db import models

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
    mileage = models.PositiveIntegerField()
    img = models.ImageField(upload_to='cars/', null=True, blank=True)
    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"

