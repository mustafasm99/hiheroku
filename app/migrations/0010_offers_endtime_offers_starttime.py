# Generated by Django 4.0.6 on 2022-10-01 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_category_item_categorys_offers_categorys'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='endTime',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='startTime',
            field=models.DateField(auto_now=True),
        ),
    ]
