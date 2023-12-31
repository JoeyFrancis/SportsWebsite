# Generated by Django 4.1.7 on 2023-05-06 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0010_alter_noticia_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('adversario', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 5, 6, 1, 46, 14, 457707, tzinfo=datetime.timezone.utc)),
        ),
    ]
