# Generated by Django 4.2.11 on 2024-03-06 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepages', '0002_product_product_category_alter_product_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='homepages/static/images'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]