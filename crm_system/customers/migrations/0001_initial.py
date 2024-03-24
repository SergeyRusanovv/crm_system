# Generated by Django 5.0.2 on 2024-03-24 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_lead', to='contracts.contract', verbose_name='Контракт')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_lead', to='leads.leads', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Активный клиент',
                'verbose_name_plural': 'Активные клиенты',
            },
        ),
    ]
