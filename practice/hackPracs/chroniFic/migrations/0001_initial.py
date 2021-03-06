# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-20 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(default='', max_length=100)),
                ('department_name', models.CharField(max_length=200)),
                ('updated_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_id', models.CharField(default='', max_length=100)),
                ('questions', models.CharField(max_length=50)),
                ('answers', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist_id', models.CharField(max_length=100)),
                ('specialist_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Department')),
            ],
        ),
        migrations.AddField(
            model_name='faq',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Specialist'),
        ),
        migrations.AddField(
            model_name='department',
            name='hospital',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Hospital'),
        ),
    ]
