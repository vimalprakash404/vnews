# Generated by Django 4.1.6 on 2023-05-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ads',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='advertiser.ads'),
            preserve_default=False,
        ),
    ]