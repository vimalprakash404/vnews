# Generated by Django 4.1.6 on 2023-04-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0005_ads_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]