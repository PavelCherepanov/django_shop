# Generated by Django 4.1.1 on 2022-09-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_product_product_brand_product_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(upload_to='static/product_img/'),
        ),
    ]