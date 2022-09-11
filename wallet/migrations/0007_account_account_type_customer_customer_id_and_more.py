# Generated by Django 4.0.6 on 2022-08-19 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_rename_amount_wallet_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('w', 'withdraw'), ('S', 'Savings'), ('D', 'Deposit')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nationality',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_picture'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet'),
        ),
    ]