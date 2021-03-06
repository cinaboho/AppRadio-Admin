# Generated by Django 2.1.1 on 2019-02-08 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebAdminRadio', '0002_auto_20190207_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='concurso',
            name='activo',
            field=models.CharField(default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='concurso',
            name='idUsuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='ganador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WebAdminRadio.Concursante'),
        ),
    ]
