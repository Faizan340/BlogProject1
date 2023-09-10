# Generated by Django 4.1.4 on 2023-01-16 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProductApp', '0002_alter_categorymodel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
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
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('total_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('ordered_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ordermodel_ordered_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordermodel_product', to='ProductApp.productmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]