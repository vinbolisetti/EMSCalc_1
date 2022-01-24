from django.db import models
from django.urls import reverse


class DRPlanningLaborCostRateModel(models.Model):
    cost = models.IntegerField()   # $ USD per hour

    def __str__(self):
        return str(self.cost)


class CPSCostModel(models.Model):
    DRPlanningLaborCostRate_USDPerHr = models.ForeignKey(DRPlanningLaborCostRateModel, on_delete=models.SET_NULL, null=True, blank=False)
    cpsHours = models.IntegerField(null=False)
    term = models.IntegerField(null=False)

    def get_cpsCalculatedCost(self):
        return self.cpsHours * self.term * self.DRPlanningLaborCostRate_USDPerHr.cost
