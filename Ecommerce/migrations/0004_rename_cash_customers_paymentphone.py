# Generated by Django 3.2.5 on 2022-07-30 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0003_auto_20220730_0309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='Cash',
            new_name='PaymentPhone',
        ),
    ]
