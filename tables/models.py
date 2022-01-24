from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


Yes = 'Yes'
No = 'No'

BOOL = (
    (Yes, Yes), (No, No),
)


class QuoteIDModel(models.Model):
    quoteID = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return str(self.quoteID)


# 1. Inputs

class CloudDeskSpecialistModel(models.Model):
    name = models.CharField(max_length=54)

    def __str__(self):
        return self.name


class CurrencyModel2(models.Model):
    name = models.CharField(max_length=5)
    exchangeRate = models.FloatField(max_length=156, null=True, blank=False)

    def __str__(self):
        return f"{self.name}: {self.exchangeRate}"


class HostingProviderModel2(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class LocationModel2(models.Model):
    hostingProvider = models.ForeignKey(HostingProviderModel2, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class QuoteInputModel2(models.Model):
    # Foreign keys
    # quoteID = models.OneToOneField(QuoteIDModel, on_delete=models.SET_NULL, null=True)
    cloudDeskSpecialist = models.ForeignKey(CloudDeskSpecialistModel, on_delete=models.SET_NULL, null=True, blank=False)
    hostingProvider = models.ForeignKey(HostingProviderModel2, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(LocationModel2, on_delete=models.SET_NULL, null=True)
    # Independent Input fields
    localCurrency = models.ForeignKey(CurrencyModel2, on_delete=models.SET_NULL, null=True, blank=False)
    cloudTermMonths = models.IntegerField(default=36)
    cloudMargin = models.FloatField(default=47.00)
    multipleActiveRegions = models.CharField(max_length=5, choices=BOOL, default='No')

    # 2a. Multi-Regions

    # gcpUS =
    # gcpNANE =
    # gcpEurope =
    # gcpAustralia =
    # gcpAsia =
    # gcpAsiaEast =
    # gcpAsiaNE =
    # gcpBrazil =

    def __str__(self):
        return f"{self.cloudDeskSpecialist}: {self.cloudTermMonths}"

    def get_absolute_url(self):
        return reverse("list_quote", kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Add Quotes'

    def get_cpsCalculatedCost(self):
        return (self.cloudTermMonths * self.cloudMargin * float(self.localCurrency.exchangeRate)).__round__(2)
