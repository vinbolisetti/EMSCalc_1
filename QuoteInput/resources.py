from import_export import resources
from .models import LocalCurrencyModel


class CurrencyResource(resources.ModelResource):
    class meta:
        model = LocalCurrencyModel
