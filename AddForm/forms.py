from django import forms
from django.forms import ModelForm

from .models import Item, Company, Chain


class ChainForm(forms.ModelForm):

    class Meta:
        model = Chain
        fields = "__all__"


class ItemMasterForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = "__all__"


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
