# Generated by Django 5.1.3 on 2025-06-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_globalpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_info',
            field=models.JSONField(default=13),
            preserve_default=False,
        ),
    ]
