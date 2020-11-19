# Generated by Django 3.0 on 2020-11-17 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0006_position_thumbnail_filename'),
        ('art', '0003_auto_20201112_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='experience.Position', verbose_name='Job where project was performed'),
        ),
    ]
