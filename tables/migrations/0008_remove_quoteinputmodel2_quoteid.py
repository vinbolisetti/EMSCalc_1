# Generated by Django 3.0.7 on 2021-04-08 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20210406_0717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteinputmodel2',
            name='quoteID',
        ),
    ]
