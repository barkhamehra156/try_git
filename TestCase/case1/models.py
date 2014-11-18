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

	priority_choices = [(i,i) for i in range(5)]
	category_choices = (('Smoke','smoke'),('Core','core'))
	story_id = models.ForeignKey(Story, db_column='StoryId')
	description_text = models.TextField(db_column = 'Description')
	category_choices = models.CharField(max_length = 25, db_column='Category',choices = category_choices)
	priority_choices = models.IntegerField(max_length = 2, db_column='Priority',choices = priority_choices)
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
	testcase_id = models.ForeignKey(TestSuiteType, db_column = 'TestCaseId', related_name = '+')
	testsuitetype_id = models.ForeignKey(TestSuiteType, db_column = 'TestSuiteTypeId')