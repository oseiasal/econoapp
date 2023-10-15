# Generated by Django 4.2.6 on 2023-10-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FinancialTransactions", "0003_alter_entry_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="BankAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_name", models.CharField(max_length=150)),
            ],
        ),
    ]
