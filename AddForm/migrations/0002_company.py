# Generated by Django 3.2 on 2021-04-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True)),
                ('short_name', models.CharField(blank=True, max_length=80, null=True)),
                ('add1', models.CharField(blank=True, max_length=150, null=True)),
                ('add2', models.CharField(blank=True, max_length=150, null=True)),
                ('add3', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('phone1', models.CharField(blank=True, max_length=12, null=True)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]