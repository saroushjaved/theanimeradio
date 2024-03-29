# Generated by Django 3.1 on 2020-08-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200815_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='List2019',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('anime_id', models.IntegerField(default=10)),
                ('summary', models.TextField(default='I am summary')),
                ('no_of_episodes', models.IntegerField(default=100)),
                ('dubbing', models.BooleanField(default=False)),
                ('images', models.ImageField(upload_to='animetitles')),
                ('rating', models.IntegerField(default=10)),
                ('link_crunchyroll', models.URLField()),
                ('link_imdb', models.URLField()),
                ('link_shop', models.URLField()),
                ('up_votes', models.IntegerField(default=10)),
                ('down_votes', models.IntegerField(default=10)),
            ],
        ),
    ]
