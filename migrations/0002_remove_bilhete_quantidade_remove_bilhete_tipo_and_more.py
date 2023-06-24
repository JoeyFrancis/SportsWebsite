# Generated by Django 4.1.7 on 2023-05-03 11:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clube', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bilhete',
            name='quantidade',
        ),
        migrations.RemoveField(
            model_name='bilhete',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='data_publicacao',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='email',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='id',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='telemovel',
        ),
        migrations.AddField(
            model_name='noticia',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 5, 3, 11, 12, 59, 689397, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='socio',
            name='foto',
            field=models.URLField(default='/votacao/static/media/user-icon.png'),
        ),
        migrations.AddField(
            model_name='socio',
            name='nr_votos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bilhete',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bilhete',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='conteudo',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telemovel', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='socio',
            name='utilizador_ptr',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clube.utilizador'),
        ),
    ]
