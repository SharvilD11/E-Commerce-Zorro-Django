# Generated by Django 4.0.6 on 2022-07-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_orderupdate_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
