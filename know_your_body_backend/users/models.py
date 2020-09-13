import uuid

from django.contrib.auth.models import User
from django.db import models


class TimeStampedUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UserBMI(TimeStampedUUIDModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)


class UserHemoglobin(TimeStampedUUIDModel):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    hemoglobin_level = models.DecimalField(max_digits=6, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GENDER)


class UserBloodSugar(TimeStampedUUIDModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    blood_sugar_level = models.DecimalField(max_digits=6, decimal_places=2)
