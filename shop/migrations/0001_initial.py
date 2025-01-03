# Generated by Django 5.1.1 on 2024-11-29 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/shop/img/')),
                ('prise', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('publisher', models.CharField(max_length=50)),
                ('tip', models.CharField(max_length=50)),
                ('Garanty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=254)),
                ('comment', models.TextField(blank=True, null=True)),
                ('count', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product')),
            ],
        ),
    ]
