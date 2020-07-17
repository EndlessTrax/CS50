from typing import cast
from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User Model
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    transactions = models.ForeignKey(
        "Transaction", on_delete=models.DO_NOTHING, null=True
    )

    def __str__(self):
        return self.username


# Transaction Model
class Transaction(models.Model):
    user_id = models.PositiveIntegerField()
    tree_id = models.PositiveIntegerField()
    sold = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-date_time"]
