from django.db import models


# Create your models here.


class Chain(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    master = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=80, unique=True, db_index=True)
    group_id = models.ForeignKey(Chain, default=37, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    short_name = models.CharField(max_length=80, null=True, blank=True)
    add1 = models.CharField(max_length=150, null=True, blank=True)
    add2 = models.CharField(max_length=150, null=True, blank=True)
    add3 = models.CharField(max_length=150, null=True, blank=True)

    city = models.CharField(max_length=60, null=True, blank=True)
    phone1 = models.CharField(max_length=12, null=True, blank=True)
    phone2 = models.CharField(max_length=12, null=True, blank=True)
