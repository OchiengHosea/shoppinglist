from django.db import models
from django.contrib.auth.models import User

class ShoppingList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    list_name = models.CharField(max_length=55)
    overall_budget = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner) + '\t' + self.list_name + '\t' + str(self.created_on)


class ShoppingItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    list_ref = models.ForeignKey(ShoppingList, on_delete=models.DO_NOTHING)
    item_name = models.CharField(max_length=55)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.IntegerField(null=True, default=1)

    def __str__(self):
        return self.item_name + '\t of' + str(self.list_ref)
    
