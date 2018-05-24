# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 02:22
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40, verbose_name='Firstname')),
                ('lname', models.CharField(max_length=40, verbose_name='Lastname')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=100, verbose_name='Firstname')),
                ('msg', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='FoodRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, verbose_name='rating')),
                ('r_status', models.CharField(choices=[('1', 'Approved'), ('2', 'Declined'), ('3', 'Pending')], default='3', max_length=200, verbose_name='status')),
                ('comments', models.TextField(verbose_name='Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=300, verbose_name='Name')),
                ('desc', models.TextField(verbose_name='Description')),
                ('other_info', models.CharField(max_length=3000, verbose_name='Other Info')),
                ('category', models.TextField(verbose_name='Categories')),
                ('price_s', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, verbose_name='Price Small')),
                ('price_m', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, verbose_name='Price Medium')),
                ('price_l', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, verbose_name='Price Large')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, verbose_name='Price')),
                ('f_status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default='1', max_length=200, verbose_name='status')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Created')),
            ],
        ),
        migrations.CreateModel(
            name='UserStamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Approved'), ('2', 'Declined'), ('3', 'Pending'), ('4', 'Claimed')], default='3', max_length=200, verbose_name='status')),
                ('order_id', models.CharField(default='000000', max_length=300, verbose_name='Order ID')),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Purchase Date')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Created')),
                ('usr', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
        ),
        migrations.AddField(
            model_name='foodrating',
            name='fid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Foods', verbose_name='Food ID'),
        ),
        migrations.AddField(
            model_name='foodrating',
            name='usr',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
    ]