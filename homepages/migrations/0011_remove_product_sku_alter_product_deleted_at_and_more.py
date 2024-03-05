# Generated by Django 4.2.11 on 2024-03-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepages', '0010_alter_product_deleted_at_alter_product_modified_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='SKU',
        ),
        migrations.AlterField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(),
        ),
    ]
