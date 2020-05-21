# Generated by Django 3.0.6 on 2020-05-21 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(blank=True, default='-', max_length=200, null=True)),
                ('lot_no', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('shape', models.CharField(choices=[('OTHER', 'OTHER'), ('AS', 'Asscher'), ('CU', 'Cushion'), ('EC', 'Emerald'), ('HS', 'Heart'), ('MQ', 'Marquise'), ('OV', 'Oval'), ('PR', 'Princess'), ('PS', 'Pear Shape'), ('RA', 'Radiant'), ('RD', 'Round')], default='OTHER', max_length=20)),
                ('carat', models.FloatField(blank=True, null=True)),
                ('stone', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(choices=[('', ''), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default='', max_length=25)),
                ('clarity', models.CharField(choices=[('FL', 'FL'), ('I1', 'I1'), ('I2', 'I2'), ('IF', 'IF'), ('SI', 'SI'), ('SI1', 'SI1'), ('SI2', 'SI2'), ('SI3', 'SI3'), ('VS', 'VS'), ('VS1', 'VS1'), ('VS2', 'VS2'), ('VVS1', 'VVS1'), ('VVS2', 'VVS2')], default='', max_length=25)),
                ('measurement', models.CharField(blank=True, max_length=50, null=True)),
                ('dept', models.FloatField(blank=True, null=True)),
                ('tbl', models.IntegerField(blank=True, null=True)),
                ('cut', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('pol', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('sym', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('fl', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('cul', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('girdle', models.CharField(blank=True, default='-', max_length=50, null=True)),
                ('lab', models.CharField(choices=[('GIA', 'GIA'), ('EGL USA', 'EGL USA'), ('OWN', 'OWN')], default='OWN', max_length=25)),
                ('certno', models.CharField(blank=True, default='-', max_length=40, null=True)),
                ('rap', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('certificate', models.URLField(blank=True, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('video', models.URLField(blank=True, default='', null=True)),
            ],
            options={
                'ordering': ['lot_no'],
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('country', models.CharField(default='India', max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
    ]
