from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.CharField(max_length=100)
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order #{self.id} - {self.item} ({self.amount})"
