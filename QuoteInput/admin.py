from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import HostingProviderModel, LocationModel, CloudDeskSpecialistModel, LocalCurrencyModel


# Register your models here.


admin.site.register(HostingProviderModel)
admin.site.register(LocationModel)
admin.site.register(CloudDeskSpecialistModel)


class CurrencyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (['name', 'exchangeRate'])


admin.site.register(LocalCurrencyModel, CurrencyAdmin)



