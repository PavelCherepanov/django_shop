# Generated by Django 4.1.1 on 2022-09-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание'),
        ),
    ]