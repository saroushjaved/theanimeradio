# Generated by Django 3.1 on 2020-08-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200814_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='list2018',
            name='down_votes',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='list2018',
            name='up_votes',
            field=models.IntegerField(default=10),
        ),
    ]
