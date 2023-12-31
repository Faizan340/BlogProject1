# Generated by Django 4.1.4 on 2023-01-24 05:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0006_useraddressmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('gid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addcartmodel_product', to='ProductApp.productmodel')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addcartmodel_stock', to='ProductApp.stockmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
