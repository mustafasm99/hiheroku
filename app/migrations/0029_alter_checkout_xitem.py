# Generated by Django 4.0.6 on 2022-10-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_checkout_copone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='xitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.item'),
        ),
    ]
