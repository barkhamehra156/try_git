# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story_name', models.CharField(max_length=200, db_column=b'StoryName')),
                ('description', models.TextField(db_column=b'Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
