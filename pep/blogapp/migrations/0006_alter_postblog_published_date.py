# Generated by Django 4.1.4 on 2023-01-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_postblog_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]