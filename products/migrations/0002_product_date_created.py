# Generated by Django 5.1.4 on 2024-12-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(null=True, verbose_name='Fecha de creación'),
        ),
    ]
