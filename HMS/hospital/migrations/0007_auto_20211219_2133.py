# Generated by Django 3.2.5 on 2021-12-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_auto_20211219_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablemedicines',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='availablemedicines',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
