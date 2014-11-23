from django.db import models

# Create your models here.


class TestEnvironment(models.Model):
	def __unicode__(self):
		return unicode(self.environment)

	environment = models.CharField(max_length = 250, db_column='Requirement')

class Story(models.Model):
	def __unicode__(self):
		return unicode(self.story_name)

	story_name = models.CharField(db_column='StoryName',max_length=200)
	description = models.TextField(db_column='Description')
	
class TestCase(models.Model):

	priority_choice_list = [(i,i) for i in range(5)]
	category_choice_list = (('Smoke','smoke'),('Core','core'))
	story_id = models.ForeignKey(Story, db_column='StoryId')
	description_text = models.TextField(db_column = 'Description')
	category_choices = models.CharField(max_length = 25, db_column='Category',choices = category_choice_list)
	priority_choices = models.IntegerField(max_length = 2, db_column='Priority',choices = priority_choice_list)
	precondition_text = models.TextField(db_column = 'Pre-Condition')
	summary_text = models.TextField(db_column = 'Summary')
	teststep_text = models.TextField(db_column = 'Test Steps')
	testdata_text = models.TextField(db_column = 'Test Data')
	expectedresult_text = models.TextField(db_column = 'Expected Result')
	testenvironment_id = models.ForeignKey(TestEnvironment, db_column = 'RequirementId')

class TestSuiteType(models.Model):
	def __unicode__(self):
		return unicode(self.suitetype)
	suitetype = models.CharField(max_length = '50', db_column = 'Suite Type')

class TestSuite(models.Model):
	def __unicode__(self):
		return unicode(self.testsuite_name)
	testsuite_name = models.CharField(max_length = '100', db_column = 'Name')
	testsuitetype_id = models.ForeignKey(TestSuiteType, db_column = 'TestSuiteTypeId')


class TestCaseSuite(models.Model):
	testcase_id = models.ForeignKey(TestCase, db_column = 'TestCaseId', related_name = '+')
	testsuite_id = models.ForeignKey(TestSuite, db_column='TestSuiteId')

class TestPlan(models.Model):
	testplan_name =  models.CharField(max_length = '100', db_column = 'Name')
	start_time = models.DateTimeField(null=True, db_column='StartTime', blank=True)
	end_time = models.DateTimeField(null=True, db_column='EndTime', blank=True)

class TestStatus(models.Model):
	status = models.CharField(max_length = 100, db_column = 'Status')

class TestPlanMap(models.Model):
	testPlan_id = models.ForeignKey(TestPlan, db_column='testPlanId')
	testcase_id = models.ForeignKey(TestCase, db_column = 'TestCaseId', related_name = '+')
	testsuite_id = models.ForeignKey(TestSuite, db_column = 'TestSuiteId', related_name = '+')
	status = models.ForeignKey(TestStatus, db_column = 'Status')
	remarks = models.TextField(db_column='Remarks')