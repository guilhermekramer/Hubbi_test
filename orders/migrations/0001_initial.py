# Generated by Django 5.1.5 on 2025-01-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=50)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products', models.ManyToManyField(blank=True, related_name='orders', to='products.products')),
            ],
        ),
    ]
