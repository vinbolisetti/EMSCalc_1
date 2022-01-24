# Generated by Django 3.2 on 2021-04-12 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0012_auto_20210409_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteinputmodel',
            name='cloudDeskSpecialist',
            field=models.ForeignKey(default='John Smith', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Quote.clouddeskspecialistmodel'),
        ),
        migrations.AlterField(
            model_name='quoteinputmodel',
            name='hostingProvider',
            field=models.ForeignKey(default='GCP', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Quote.hostingprovidermodel'),
        ),
        migrations.AlterField(
            model_name='quoteinputmodel',
            name='localCurrency',
            field=models.ForeignKey(default='USD: 1.0', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Quote.currencymodel'),
        ),
        migrations.AlterField(
            model_name='quoteinputmodel',
            name='location',
            field=models.ForeignKey(default='GCP Canada', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Quote.locationmodel'),
        ),
        migrations.AlterField(
            model_name='quoteinputmodel',
            name='multipleActiveRegions',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5),
        ),
    ]