# Generated by Django 4.0.6 on 2022-08-19 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_alter_card_card_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='customer',
        ),
        migrations.AddField(
            model_name='wallet',
            name='account_wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_wallet', to='wallet.account'),
        ),
    ]
