# Generated by Django 4.0.5 on 2022-06-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrm', '0009_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('Lead', 'Lead'), ('Female', 'Contact')], default='Contact', max_length=200),
        ),
    ]