# Generated by Django 2.2.1 on 2019-06-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ushort', '0002_url_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='hash',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.TextField(unique=True),
        ),
    ]
