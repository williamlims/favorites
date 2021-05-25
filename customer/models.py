from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['id']

    def __str__(self):
        return self.name

class FavoriteList(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        unique_together = ['customer_id', 'product_id']
        ordering = ['id']
