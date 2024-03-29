# Generated by Django 5.0.2 on 2024-03-24 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('channel', models.CharField(max_length=50, verbose_name='Канал продвижения')),
                ('budget', models.DecimalField(decimal_places=3, max_digits=10, max_length=10, verbose_name='Бюджет на рекламу')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisings', to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Рекламная компания',
                'verbose_name_plural': 'Рекламные компании',
            },
        ),
    ]
