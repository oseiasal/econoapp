# Generated by Django 4.2.6 on 2023-10-15 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("FinancialTransactions", "0004_bankaccount"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="account",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="FinancialTransactions.bankaccount",
            ),
        ),
    ]
