# Generated by Django 5.0.2 on 2024-02-14 12:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_product_is_hidden_product_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('session_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='orders.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.product')),
            ],
        ),
    ]
