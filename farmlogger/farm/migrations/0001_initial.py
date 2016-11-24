# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 01:01
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('event', models.CharField(choices=[('user:create', 'user:create'), ('user:delete', 'user:delete'), ('field:create', 'field:create'), ('field:update', 'field:update'), ('field:delete', 'field:delete'), ('planting:create', 'planting:create'), ('fertilizing:create', 'fertilizing:create'), ('rainfall', 'rainfall')], max_length=100)),
                ('entity', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('acres', models.IntegerField()),
                ('crop', models.CharField(max_length=255)),
                ('total_rainfall', models.FloatField(null=True)),
                ('last_rainfall', models.DateTimeField(null=True)),
                ('fertilizer_type', models.CharField(max_length=50)),
                ('fertilization_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.User'),
        ),
        migrations.AddField(
            model_name='field',
            name='fertilized_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fertilizations', to='farm.User'),
        ),
        migrations.AddField(
            model_name='field',
            name='planted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantings', to='farm.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='fields',
            field=models.ManyToManyField(to='farm.Field'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farm.User'),
        ),
    ]
