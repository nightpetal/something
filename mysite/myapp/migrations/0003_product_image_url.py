# Generated by Django 5.2.4 on 2025-07-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_alter_product_id_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(max_length=300, null=True),
        ),
    ]
