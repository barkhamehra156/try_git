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
                ('title', models.CharField(max_length=100, db_column=b'Title')),
                ('category', models.CharField(max_length=25, db_column=b'Category', choices=[(b'Smoke', b'smoke'), (b'Core', b'core')])),
                ('priority', models.IntegerField(max_length=2, db_column=b'Priority', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])),
                ('precondition', models.TextField(verbose_name=b'Pre-Condition', db_column=b'PreCondition')),
                ('summary', models.TextField(db_column=b'Summary')),
                ('test_step', models.TextField(verbose_name=b'Test Step', db_column=b'TestSteps')),
                ('testdata', models.TextField(verbose_name=b'Test Data', db_column=b'TestData')),
                ('expected_result', models.TextField(verbose_name=b'Expected Result', db_column=b'ExpectedResult')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCaseSuite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            name='TestPlanCaseMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remarks', models.TextField(null=True, db_column=b'Remarks', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestPlanSuiteMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remarks', models.TextField(null=True, db_column=b'Remarks', blank=True)),
                ('testPlan_id', models.ForeignKey(to='dashboard.TestPlan', db_column=b'testPlanId')),
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
                ('suiteType', models.CharField(max_length=b'50', db_column=b'SuiteType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testsuite',
            name='testSuitType',
            field=models.ForeignKey(to='dashboard.TestSuiteType', db_column=b'TestSuiteTypeId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplansuitemap',
            name='testsuite_id',
            field=models.ForeignKey(related_name='+', db_column=b'TestSuiteId', to='dashboard.TestSuite'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplancasemap',
            name='status',
            field=models.ForeignKey(to='dashboard.TestStatus', db_column=b'Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplancasemap',
            name='testPlan_id',
            field=models.ForeignKey(to='dashboard.TestPlan', db_column=b'testPlanId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testplancasemap',
            name='testcase_id',
            field=models.ForeignKey(related_name='+', db_column=b'TestCaseId', to='dashboard.TestCase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcasesuite',
            name='status',
            field=models.ForeignKey(db_column=b'Status', blank=True, to='dashboard.TestStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcasesuite',
            name='testcase_id',
            field=models.ForeignKey(related_name='+', db_column=b'TestCaseId', to='dashboard.TestCase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcasesuite',
            name='testsuite_id',
            field=models.ForeignKey(to='dashboard.TestSuite', db_column=b'TestSuiteId'),
            preserve_default=True,
        ),
    ]
