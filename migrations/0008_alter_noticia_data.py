# Generated by Django 4.1.7 on 2023-05-06 01:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0007_game_delete_jogo_alter_noticia_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 5, 6, 1, 10, 41, 159432, tzinfo=datetime.timezone.utc)),
        ),
    ]
