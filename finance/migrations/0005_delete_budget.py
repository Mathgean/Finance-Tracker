# Generated by Django 5.0.1 on 2024-02-17 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_budget_budget_limit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Budget',
        ),
    ]
