# Generated by Django 5.0.1 on 2024-02-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='budget_limit',
            field=models.IntegerField(default=25000),
        ),
    ]
