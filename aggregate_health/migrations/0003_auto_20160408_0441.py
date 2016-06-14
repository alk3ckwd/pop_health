# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 04:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggregate_health', '0002_primarycareprovider_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_performed', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate_health.Patient')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate_health.PrimaryCareProvider')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate_health.Condition')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate_health.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='VisitTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='encounter',
            name='visit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate_health.VisitTypes'),
        ),
    ]