# Generated by Django 3.0.7 on 2020-10-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201020_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, to='accounts.Tag'),
        ),
    ]
