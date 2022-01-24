from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import CurrencyModel, CloudDeskSpecialistModel, QuoteInputModel, HostingProviderModel, LocationModel


admin.site.register(CloudDeskSpecialistModel)
admin.site.register(QuoteInputModel)
admin.site.register(HostingProviderModel)
admin.site.register(LocationModel)


class CurrencyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (['name', 'exchangeRate'])


admin.site.register(CurrencyModel, CurrencyAdmin)

