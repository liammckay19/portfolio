# Generated by Django 3.0 on 2020-11-17 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0004_auto_20201117_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='upload',
            field=models.ImageField(blank=True, null=True, storage='images/', upload_to='images'),
        ),
    ]
