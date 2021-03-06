# Generated by Django 3.1.7 on 2021-02-24 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contudo_post',
            new_name='conteudo_post',
        ),
        migrations.AlterField(
            model_name='post',
            name='autor_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de publicação'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo_post',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
    ]
