# Generated by Django 2.2.1 on 2019-06-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ushort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
