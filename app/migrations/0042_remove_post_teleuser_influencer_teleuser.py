# Generated by Django 4.0.6 on 2022-10-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_brand_teleuser_post_teleuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='teleuser',
        ),
        migrations.AddField(
            model_name='influencer',
            name='teleuser',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
