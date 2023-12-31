# Generated by Django 4.1.4 on 2023-01-27 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0009_ordermodel_addcart_remove_addcartmodel_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('0', 'Yes'), ('1', 'No')], max_length=1, null=True)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ordermodel_order', to='ProductApp.ordermodel')),
            ],
        ),
    ]
