# Generated by Django 4.0.5 on 2022-06-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrm', '0007_channel_alter_interaction_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='contact',
            name='image_url',
            field=models.CharField(default='/static/ocrm/img/generic-customer.jpg', max_length=1000),
        ),
        migrations.AlterField(
            model_name='ownedproduct',
            name='purchase_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
