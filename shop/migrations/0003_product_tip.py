# Generated by Django 5.1.1 on 2024-10-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tip',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]