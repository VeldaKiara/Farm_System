# Generated by Django 3.0.7 on 2020-07-22 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0002_cart_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_items',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_paid', models.BinaryField(default=False)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
            ],
        ),
    ]