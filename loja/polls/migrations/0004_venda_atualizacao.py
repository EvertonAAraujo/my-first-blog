# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_cliente_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='atualizacao',
            field=models.DateTimeField(default='2017-11-21 12:00', auto_now=True),
            preserve_default=False,
        ),
    ]
