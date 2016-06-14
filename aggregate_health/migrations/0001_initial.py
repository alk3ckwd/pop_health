# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField()),
                ('gender', models.CharField(max_length=1)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryCareProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('npi', models.IntegerField()),
                ('clinicSite', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='primarycareprovider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate_health.PrimaryCareProvider'),
        ),
    ]
