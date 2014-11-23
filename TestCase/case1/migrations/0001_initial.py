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
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_text', models.TextField(db_column=b'Description')),
                ('category_choices', models.CharField(max_length=25, db_column=b'Category', choices=[(b'Smoke', b'smoke'), (b'Core', b'core')])),
                ('priority_choices', models.IntegerField(max_length=2, db_column=b'Priority', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])),
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
            name='TestCaseSuite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testcase_id', models.ForeignKey(related_name='+', db_column=b'TestCaseId', to='case1.TestCase')),
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
            name='TestPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testplan_name', models.CharField(max_length=b'100', db_column=b'Name')),
                ('start_time', models.DateTimeField(null=True, db_column=b'StartTime', blank=True)),
                ('end_time', models.DateTimeField(null=True, db_column=b'EndTime', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestPlanMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remarks', models.TextField(db_column=b'Remarks')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=100, db_column=b'Status')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testsuite_name', models.CharField(max_length=b'100', db_column=b'Name')),
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
            name='testsuitetype_id',
            field=models.ForeignKey(to='case1.TestSuiteType', db_column=b'TestSuiteTypeId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplanmap',
            name='status',
            field=models.ForeignKey(to='case1.TestStatus', db_column=b'Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplanmap',
            name='testPlan_id',
            field=models.ForeignKey(to='case1.TestPlan', db_column=b'testPlanId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplanmap',
            name='testcase_id',
            field=models.ForeignKey(related_name='+', db_column=b'TestCaseId', to='case1.TestCase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplanmap',
            name='testsuite_id',
            field=models.ForeignKey(related_name='+', db_column=b'TestSuiteId', to='case1.TestSuite'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcasesuite',
            name='testsuite_id',
            field=models.ForeignKey(to='case1.TestSuite', db_column=b'TestSuiteId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcase',
            name='testenvironment_id',
            field=models.ForeignKey(to='case1.TestEnvironment', db_column=b'RequirementId'),
            preserve_default=True,
        ),
    ]
