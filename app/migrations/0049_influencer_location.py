# Generated by Django 4.1.3 on 2022-12-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_influncerrequest_adimnaccept_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]