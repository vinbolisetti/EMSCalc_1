# Generated by Django 3.2 on 2021-04-08 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0004_auto_20210408_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quoteidmodel',
            old_name='quoteID',
            new_name='name',
        ),
    ]