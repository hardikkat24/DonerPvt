# Generated by Django 3.0.7 on 2020-07-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200715_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]