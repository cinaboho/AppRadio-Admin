# Generated by Django 2.1.1 on 2019-02-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0004_pregunta_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='tipo',
            field=models.CharField(default='E', max_length=1),
        ),
    ]
