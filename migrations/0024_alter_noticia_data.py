# Generated by Django 4.1.7 on 2023-05-08 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0023_noticia_imagem_alter_noticia_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 5, 8, 12, 38, 55, 820174, tzinfo=datetime.timezone.utc)),
        ),
    ]