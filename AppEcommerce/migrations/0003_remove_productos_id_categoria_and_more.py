# Generated by Django 5.0 on 2024-01-19 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEcommerce', '0002_alter_productos_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='id_categoria',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='id_marca',
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppEcommerce.productoscategorias'),
            preserve_default=False,
        ),
    ]