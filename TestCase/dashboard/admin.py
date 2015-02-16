from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse
from django.forms.models import BaseInlineFormSet
from dashboard.models import TestEnvironment, Story, TestCase, TestSuiteType, TestSuite, TestCaseSuite
from dashboard.models import TestPlan , TestStatus, TestPlanSuiteMap, TestPlanCaseMap
from django.db import models
#class TestCaseInline(admin.TabularInline):
#    model = TestCase
#    extra = 1
#

class CustomInlineTestPlanSuite(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            print form

class StoryAdmin(admin.ModelAdmin):
	list_display = ('story_name', 'description')

class TestStatusAdmin(admin.ModelAdmin):
	list_display = ('status',)

class TestCaseSuiteInline(admin.TabularInline):
    model = TestCaseSuite
    extra = 1

class TestPlanSuiteInline(admin.TabularInline):
    model = TestPlanSuiteMap
    exclude = ('testcase_id',)
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 2, 'cols': 70})},
    }
    extra = 1

class TestPlanCaseInline(admin.TabularInline):
    model = TestPlanCaseMap
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 2, 'cols': 70})},
    }
    extra = 1
    
class TestCaseAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title']}),
                 ('Test Case Type', {'fields': ['category','priority']}),
                 ('Test Case Specification', {'fields': ['precondition', 'test_step', 'testdata', 'summary', 'expected_result']})
                ]
    list_display = ('title', 'priority', 'category')
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 2, 'cols': 100})},
    }
    
#class TestCaseInlineAdmin(admin.TabularInline):
#    model = tcase
#    def get_testCases(self):
#        if self.testCase:
#            return '%s' % " \n ".join([testCase.title for testCase in self.testCase.all()])
#  
#class MembershipInline(admin.TabularInline):
#    model = TestSuite.testCase.through

#class TestCaseAdmin(admin.ModelAdmin):
#    inlines = [MembershipInline,] 
         
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ('testsuite_name',)
#    fields = ['list_display']
    inlines=(TestCaseSuiteInline,)
#    def test_cases(self, obj):
#        #return "\n".join([p for p in self.inlines.all()])
#        return u""
#        return "\n".join([str(p+1)+"<html><p>-----------------------------</p></html>\n" for p in range(5)])
        
    def foo_link(self, obj):
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print obj.pk
        url = reverse('admin:case1_TestCaseSuite_changelist')#, args=(obj.pk,)
        print url
        return '<a href="%s">See Test Case Suite</a>' % url 
#    foo_link.allow_tags = True
  
class TestEnvironmentAdmin(admin.ModelAdmin):
	list_display = ('environment',)
 
class TestPlanAdmin(admin.ModelAdmin):
    list_display = ('testplan_name', 'start_time', 'end_time')
    inlines=(TestPlanSuiteInline,TestPlanCaseInline)
 
admin.site.register(TestCase,TestCaseAdmin)
admin.site.register(Story,StoryAdmin)
admin.site.register(TestSuiteType)
admin.site.register(TestSuite, TestSuiteAdmin)
admin.site.register(TestEnvironment,TestEnvironmentAdmin)
admin.site.register(TestCaseSuite)
admin.site.register(TestPlan,TestPlanAdmin)
admin.site.register(TestStatus)
