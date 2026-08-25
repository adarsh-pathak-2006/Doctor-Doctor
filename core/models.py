from django.db import models
from django.contrib.auth.models import User


class Prescription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    condition=models.TextField()
    prior_medical_history=models.TextField()
    drug_prescription=models.TextField()
    analysis=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

