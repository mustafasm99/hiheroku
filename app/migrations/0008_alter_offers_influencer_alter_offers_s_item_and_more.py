# Generated by Django 4.0.6 on 2022-09-30 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_offers_influencer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='influencer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.influencer'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='s_item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.item'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='woner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
    ]