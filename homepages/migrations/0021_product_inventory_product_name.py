# Generated by Django 4.2.11 on 2024-03-05 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepages', '0020_alter_discount_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_inventory',
            name='product_name',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='homepages.product'),
            preserve_default=False,
        ),
    ]
