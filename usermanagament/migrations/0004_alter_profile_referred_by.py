# Generated by Django 5.1.3 on 2025-02-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagament', '0003_profile_referral_link_profile_referred_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='referred_by',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
