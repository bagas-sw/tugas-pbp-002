# Generated by Django 4.1 on 2022-09-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_alter_mywatchlist_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='watched',
            field=models.BooleanField(),
        ),
    ]
