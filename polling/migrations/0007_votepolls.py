# Generated by Django 3.1.1 on 2020-09-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0006_choices_choicedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotePolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0)),
                ('poll', models.IntegerField(default=0)),
            ],
        ),
    ]
