# Generated by Django 3.0.7 on 2021-04-03 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudDeskSpecialistModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54)),
            ],
        ),
        migrations.AddField(
            model_name='quoteinputmodel2',
            name='cloudDeskSpecialist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.CloudDeskSpecialistModel'),
        ),
    ]
