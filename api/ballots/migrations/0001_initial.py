# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elections', '0003_blank_regions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Parties',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('seats', models.PositiveIntegerField(default=1)),
                ('candidates', models.ManyToManyField(blank=True, to='ballots.Candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Election')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Election')),
                ('regions', models.ManyToManyField(to='elections.Region')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ballots.Party'),
        ),
    ]
