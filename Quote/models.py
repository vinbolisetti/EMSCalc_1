from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings


Yes = 'Yes'
No = 'No'

BOOL = (
    (Yes, Yes), (No, No),
)


'''class QuoteIDModel(models.Model):
    quoteID = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return str(self.quoteID)'''


# 1. Inputs

class CloudDeskSpecialistModel(models.Model):
    name = models.CharField(max_length=54)

    def __str__(self):
        return self.name


class CurrencyModel(models.Model):
    name = models.CharField(max_length=5)
    exchangeRate = models.FloatField(max_length=156, null=True, blank=False)

    def __str__(self):
        return f"{self.name}: {self.exchangeRate}"


class HostingProviderModel(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class LocationModel(models.Model):
    hostingProvider = models.ForeignKey(HostingProviderModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class QuoteInputModel(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_NULL, null=True)
    # Foreign keys
    # quoteID = models.OneToOneField(QuoteIDModel, on_delete=models.SET_NULL, null=True)

    createdDate = models.DateTimeField(auto_now=True)
    cloudDeskSpecialist = models.ForeignKey(CloudDeskSpecialistModel, on_delete=models.SET_NULL, null=True, blank=False, default='John Smith')
    hostingProvider = models.ForeignKey(HostingProviderModel, on_delete=models.SET_NULL, null=True, blank=False)
    location = models.ForeignKey(LocationModel, on_delete=models.SET_NULL, null=True, blank=True)
    # Independent Input fields
    localCurrency = models.ForeignKey(CurrencyModel, on_delete=models.SET_NULL, null=True, blank=False, default='USD: 1.0')
    cloudTermMonths = models.IntegerField(default=36)
    cloudMargin = models.FloatField(default=47.00)
    multipleActiveRegions = models.CharField(max_length=5, choices=BOOL)


    # 2a. Multi-Regions

    gcpUS = models.CharField(max_length=5, choices=BOOL, blank=False)
    gcpAustralia = models.CharField(max_length=5, choices=BOOL, blank=True)
    gcpCanada = models.CharField(max_length=5, choices=BOOL, blank=True)
    opentextAustralia = models.CharField(max_length=5, choices=BOOL, blank=True)
    opentextCanada = models.CharField(max_length=5, choices=BOOL, blank=True)

    def __str__(self):
        return f"{self.cloudDeskSpecialist}: {self.cloudTermMonths}"

    def get_absolute_url(self):
        return reverse("list_quote", kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Add Quotes'

    def get_cpsCalculatedCost(self):
        return (self.cloudTermMonths * self.cloudMargin * float(self.localCurrency.exchangeRate)).__round__(2)
