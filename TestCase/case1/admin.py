from django.contrib import admin
from case1.models import TestEnvironment, Story, TestCase, TestSuiteType, TestSuite, TestCaseSuite, TestPlan , TestPlanMap, TestStatus

class StoryAdmin(admin.ModelAdmin):
	list_display = ('story_name', 'description')

class TestCaseSuiteAdmin(admin.ModelAdmin):
	list_display = ('TestCaseId', 'TestSuiteId')

admin.site.register(TestCase)
admin.site.register(Story,StoryAdmin)
admin.site.register(TestSuiteType)
admin.site.register(TestSuite)
admin.site.register(TestEnvironment)
admin.site.register(TestCaseSuite)
admin.site.register(TestPlan)
admin.site.register(TestPlanMap)
admin.site.register(TestStatus)
# Register your models here.
