# Generated by Django 3.0.7 on 2020-07-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200715_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='mobile_no',
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
