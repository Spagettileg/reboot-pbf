# Generated by Django 2.0.2 on 2020-01-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200124_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
