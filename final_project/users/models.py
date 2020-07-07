from typing import cast
from django.contrib.auth.models import AbstractUser
from django.db import models

from trees.models import Tree


# Custom User Model
class CustomUser(AbstractUser):
    transactions = models.ForeignKey(Transaction.id, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.username


# Transaction Model
class Transaction(models.Model):
    user_id = models.OneToOneField(CustomUser.pk, on_delete=models.DO_NOTHING)
    tree_id = models.OneToOneField(Tree.id, on_delete=models.DO_NOTHING)
    sold = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id