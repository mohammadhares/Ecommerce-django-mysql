# Generated by Django 3.2.5 on 2022-10-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0007_orders_shipping_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='seller_id',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='products',
            name='seller_id',
            field=models.CharField(default=0, max_length=200),
        ),
    ]