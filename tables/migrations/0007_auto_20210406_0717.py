# Generated by Django 3.0.7 on 2021-04-06 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_quoteinputmodel2_multipleactiveregions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteinputmodel2',
            name='multipleActiveRegions',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5),
        ),
    ]
