# Generated by Django 3.1.2 on 2021-02-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
