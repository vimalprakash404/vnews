# Generated by Django 4.1.6 on 2023-05-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0008_payment_ads'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
