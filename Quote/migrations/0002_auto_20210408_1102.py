# Generated by Django 3.2 on 2021-04-08 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CurrencyModel2',
            new_name='CurrencyModel',
        ),
        migrations.RenameModel(
            old_name='HostingProviderModel2',
            new_name='HostingProviderModel',
        ),
        migrations.RenameModel(
            old_name='LocationModel2',
            new_name='LocationModel',
        ),
        migrations.RenameModel(
            old_name='QuoteInputModel2',
            new_name='QuoteInputModel',
        ),
    ]