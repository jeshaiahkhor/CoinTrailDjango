# Generated by Django 5.0.4 on 2024-05-12 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_track', '0002_alter_transaction_category_alter_transaction_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='from_account',
            new_name='income_account',
        ),
    ]
