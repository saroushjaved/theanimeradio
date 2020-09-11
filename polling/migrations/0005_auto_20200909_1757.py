# Generated by Django 3.1.1 on 2020-09-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0004_polls_poll_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='poll_image',
            field=models.ImageField(default=2, upload_to='polltitles'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choices',
            name='image',
            field=models.ImageField(upload_to='animetitles'),
        ),
    ]