# Generated by Django 5.1.1 on 2024-10-01 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_add_slug_to_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
