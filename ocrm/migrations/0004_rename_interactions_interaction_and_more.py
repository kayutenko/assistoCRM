# Generated by Django 4.0.5 on 2022-06-10 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocrm', '0003_product_ownedproducts_interactions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Interactions',
            new_name='Interaction',
        ),
        migrations.RenameModel(
            old_name='OwnedProducts',
            new_name='OwnedProduct',
        ),
    ]
