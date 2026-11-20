from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    registration_number= models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    owner = models.ForeignKey(
        Owner, 
        on_delete=models.CASCADE, 
        related_name='cars', 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
