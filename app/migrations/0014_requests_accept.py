# Generated by Django 4.0.6 on 2022-10-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_requests_brand_requests_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='Accept',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]