from django.db import models
from django.contrib.auth.models import User 

class Participate(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Participate ID: {self.id} {self.user.first_name} {self.user.email}"

class Host(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Host ID: {self.id} {self.user.first_name} {self.user.email}"
