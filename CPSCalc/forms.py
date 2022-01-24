from django import forms
from .models import CPSCostModel, DRPlanningLaborCostRateModel


class CPSCostForm(forms.ModelForm):
    class Meta:
        model = CPSCostModel
        fields = '__all__'


class DRPlanningLaborCostRateForm(forms.ModelForm):
    class Meta:
        model = DRPlanningLaborCostRateModel
        fields = '__all__'
