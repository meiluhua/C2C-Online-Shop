# Generated by Django 3.2 on 2022-03-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20220303_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]