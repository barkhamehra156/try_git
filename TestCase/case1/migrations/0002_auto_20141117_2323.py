# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_text', models.TextField(db_column=b'Description')),
                ('category_choices', models.CharField(max_length=25, db_column=b'Category', choices=[(b'Smoke', b'smoke'), (b'Core', b'core')])),
                ('priority_choices', models.CharField(max_length=2, db_column=b'Priority', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])),
                ('precondition_text', models.TextField(db_column=b'Pre-Condition')),
                ('summary_text', models.TextField(db_column=b'Summary')),
                ('teststep_text', models.TextField(db_column=b'Test Steps')),
                ('testdata_text', models.TextField(db_column=b'Test Data')),
                ('expectedresult_text', models.TextField(db_column=b'Expected Result')),
                ('story_id', models.ForeignKey(to='case1.Story', db_column=b'StoryId')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestEnvironment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('environment', models.CharField(max_length=250, db_column=b'Requirement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestSuiteType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suitetype', models.CharField(max_length=b'50', db_column=b'Suite Type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testsuite',
            name='testcase_id',
            field=models.ForeignKey(related_name='+', db_column=b'TestCaseId', to='case1.TestSuiteType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testsuite',
            name='testsuitetype_id',
            field=models.ForeignKey(to='case1.TestSuiteType', db_column=b'TestSuiteTypeId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcase',
            name='testenvironment_id',
            field=models.ForeignKey(to='case1.TestEnvironment', db_column=b'RequirementId'),
            preserve_default=True,
        ),
    ]
