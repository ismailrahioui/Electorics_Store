# Generated by Django 5.1.2 on 2024-11-17 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_app', '0004_images_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='Price',
            field=models.CharField(choices=[('1000 to 2000', '1000 to 2000'), ('2000 to 3000', '2000 to 3000'), ('3000 to 4000', '3000 to 4000'), ('4000 to 5000', '4000 to 5000'), ('5000 to 6000', '5000 to 6000')], max_length=60),
        ),
    ]