# Generated by Django 4.1.2 on 2022-10-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_remove_post_teleuser_influencer_teleuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='followers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='following',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]