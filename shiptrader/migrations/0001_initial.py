# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('hyperdrive_rating', models.FloatField()),
                ('cargo_capacity', models.BigIntegerField()),
                ('crew', models.IntegerField()),
                ('passengers', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='ship_type',
            field=models.ForeignKey(related_name='listings', to='shiptrader.Starship'),
        ),
    ]
