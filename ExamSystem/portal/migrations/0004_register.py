# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mail', models.CharField(max_length=500)),
                ('password_R', models.CharField(max_length=250)),
                ('phone_no', models.IntegerField()),
                ('address', models.TextField(max_length=1000)),
            ],
        ),
    ]