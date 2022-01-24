from import_export import resources
from .models import CurrencyModel


class CurrencyResource(resources.ModelResource):
    class meta:
        model = CurrencyModel
