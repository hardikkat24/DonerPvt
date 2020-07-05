# Generated by Django 3.0.7 on 2020-06-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200601_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default='D', max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='cut',
            field=models.CharField(blank=True, choices=[('GIA', 'GIA'), ('EGL USA', 'EGL USA'), ('OWN', 'OWN')], default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fl',
            field=models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pol',
            field=models.CharField(blank=True, choices=[('GIA', 'GIA'), ('EGL USA', 'EGL USA'), ('OWN', 'OWN')], default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sym',
            field=models.CharField(blank=True, choices=[('GIA', 'GIA'), ('EGL USA', 'EGL USA'), ('OWN', 'OWN')], default='-', max_length=10, null=True),
        ),
    ]