# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcasesuite',
            name='status',
        ),
        migrations.AddField(
            model_name='testplansuitemap',
            name='testcase_id',
            field=models.ForeignKey(related_name='+', db_column=b'TestCaseId', default=1, to='dashboard.TestCase'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='description',
            field=models.TextField(null=True, db_column=b'Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='category',
            field=models.CharField(blank=True, max_length=25, null=True, db_column=b'Category', choices=[(b'Smoke', b'smoke'), (b'Core', b'core')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='expected_result',
            field=models.TextField(null=True, verbose_name=b'Expected Result', db_column=b'ExpectedResult', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='precondition',
            field=models.TextField(null=True, verbose_name=b'Pre-Condition', db_column=b'PreCondition', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='priority',
            field=models.IntegerField(blank=True, max_length=2, null=True, db_column=b'Priority', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='summary',
            field=models.TextField(null=True, db_column=b'Summary', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='test_step',
            field=models.TextField(null=True, verbose_name=b'Test Step', db_column=b'TestSteps', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='testdata',
            field=models.TextField(null=True, verbose_name=b'Test Data', db_column=b'TestData', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testplancasemap',
            name='status',
            field=models.ForeignKey(db_column=b'Status', blank=True, to='dashboard.TestStatus', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='testSuitType',
            field=models.ForeignKey(db_column=b'TestSuiteTypeId', blank=True, to='dashboard.TestSuiteType', null=True),
            preserve_default=True,
        ),
    ]
