# Generated by Django 2.2.1 on 2019-06-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='icons',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
