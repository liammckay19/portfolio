# Generated by Django 3.0 on 2020-11-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0007_auto_20201117_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='upload',
            field=models.ImageField(upload_to='science'),
        ),
    ]
