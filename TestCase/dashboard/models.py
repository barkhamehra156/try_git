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
	description = models.TextField(db_column='Description', blank=True, null=True)

class TestSuiteType(models.Model):
	def __unicode__(self):
		return unicode(self.suiteType)
  
	suiteType = models.CharField(max_length = '50', db_column = 'SuiteType')
 
class TestCase(models.Model):
    def __unicode__(self):
		return unicode(self.title)+ (u' - '+ unicode(self.summary[:30]) + (u'...' if len(self.summary)>30 else '') if self.summary else "")
    priority_choice = [(i,i) for i in range(5)]
    category_choice = (('Smoke','smoke'),('Core','core'))
    title = models.CharField(max_length = 100,db_column = 'Title')
    category = models.CharField(max_length = 25, db_column='Category',choices = category_choice, blank=True, null=True)
    priority = models.IntegerField(max_length = 2, db_column='Priority',choices = priority_choice, blank=True, null=True)
    precondition = models.TextField(db_column = 'PreCondition', verbose_name='Pre-Condition', blank=True, null=True)
    summary = models.TextField(db_column = 'Summary', blank=True, null=True)
    test_step = models.TextField(db_column = 'TestSteps', verbose_name='Test Step', blank=True, null=True)
    testdata = models.TextField(db_column = 'TestData', verbose_name='Test Data', blank=True, null=True)
    expected_result = models.TextField(db_column = 'ExpectedResult', verbose_name='Expected Result', blank=True, null=True)
#    testSuite = models.ManyToManyField(TestSuite,blank=True,null=True,related_name='TestCases')

class TestSuite(models.Model):
    def __unicode__(self):
        return unicode(self.testsuite_name)
    testsuite_name = models.CharField(max_length = '100', db_column = 'Name')
    testSuitType = models.ForeignKey(TestSuiteType, db_column = 'TestSuiteTypeId', blank=True, null=True)
        #testCase = models.ManyToManyField(TestCase,blank=True,null=True,related_name='TestSuites')
        
#        def get_testCases(self):
#            if self.testCase:
#                return '%s' % " \n ".join([testCase.title for testCase in self.testCase.all()])

class TestStatus(models.Model):
    def __unicode__(self):
        return unicode(self.status)
    status = models.CharField(max_length = 100, db_column = 'Status') 

class TestCaseSuite(models.Model):
    def __unicode__(self):
        return unicode(self.testsuite_id) +u' - ' +unicode(self.testcase_id)
    testcase_id = models.ForeignKey(TestCase, db_column = 'TestCaseId', related_name = '+')
    testsuite_id = models.ForeignKey(TestSuite, db_column='TestSuiteId')

class TestPlan(models.Model):
    def __unicode__(self):
        return unicode(self.testplan_name)
    testplan_name =  models.CharField(max_length = '100', db_column = 'Name')
    start_time = models.DateTimeField(null=True, db_column='StartTime', blank=True)
    end_time = models.DateTimeField(null=True, db_column='EndTime', blank=True)

class TestPlanCaseMap(models.Model):
    def __unicode__(self):
        return unicode(self.testPlan_id) +u' - ' +unicode(self.testcase_id)
    testPlan_id = models.ForeignKey(TestPlan, db_column='testPlanId')
    testcase_id = models.ForeignKey(TestCase, db_column = 'TestCaseId', related_name = '+')
    status = models.ForeignKey(TestStatus, db_column = 'Status', blank=True, null=True)
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)
 
class TestPlanSuiteMap(models.Model):
    def __unicode__(self):
            return unicode(self.testPlan_id) +u' - ' +unicode(self.testsuite_id)
    testPlan_id = models.ForeignKey(TestPlan, db_column='testPlanId')
    testsuite_id = models.ForeignKey(TestSuite, db_column = 'TestSuiteId', related_name = '+')
    testcase_id = models.ForeignKey(TestCase, db_column = 'TestCaseId', related_name = '+')
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)