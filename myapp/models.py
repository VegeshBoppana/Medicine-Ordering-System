from django.db import models
 
class Medicines(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name