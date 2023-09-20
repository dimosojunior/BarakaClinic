# Generated by Django 3.2.5 on 2021-12-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_availablemedicines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablemedicines',
            name='created',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='availablemedicines',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description 1'),
        ),
    ]