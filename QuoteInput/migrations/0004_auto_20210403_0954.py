# Generated by Django 3.0.7 on 2021-04-03 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteInput', '0003_auto_20210403_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteinputmodel',
            name='quoteName',
            field=models.CharField(max_length=56, null=True),
        ),
        migrations.DeleteModel(
            name='QuoteNameModel',
        ),
    ]
