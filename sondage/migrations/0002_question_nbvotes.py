# Generated by Django 4.2.3 on 2023-07-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sondage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='nbvotes',
            field=models.IntegerField(default=0),
        ),
    ]
