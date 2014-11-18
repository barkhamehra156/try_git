from django.contrib import admin
from case1.models import TestEnvironment, Story, TestCase, TestSuiteType, TestSuite

class StoryAdmin(admin.ModelAdmin):
	list_display = ('story_name', 'description')

admin.site.register(TestCase)
admin.site.register(Story,StoryAdmin)
admin.site.register(TestSuiteType)
admin.site.register(TestSuite)
admin.site.register(TestEnvironment)
# Register your models here.
