# Generated by Django 4.0.5 on 2022-06-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrm', '0011_delete_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('Lead', 'Lead'), ('Contact', 'Contact')], default='Contact', max_length=200),
        ),
    ]
