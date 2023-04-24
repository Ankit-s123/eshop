# Generated by Django 4.1.1 on 2023-02-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_buyer_pic4_alter_product_pic1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, default='In Stock', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
