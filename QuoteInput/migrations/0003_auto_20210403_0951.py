# Generated by Django 3.0.7 on 2021-04-03 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteInput', '0002_auto_20210403_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteNameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
            ],
        ),
        migrations.AlterField(
            model_name='quoteinputmodel',
            name='quoteName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuoteInput.QuoteNameModel'),
        ),
    ]
