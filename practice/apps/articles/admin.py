from django.contrib import admin


from practice.apps.articles.models import Category
from practice.apps.articles.models import Article



admin.site.register(Category)
admin.site.register(Article)
# Register your models here.


#from polls.models import Poll, Choice
#
#
#class ChoiceInline(admin.TabularInline):
#	model = Choice
#	extra = 3
#
#class PollAdmin(admin.ModelAdmin):
#	fieldsets = [
#		('KIRVY', 			 {'fields': ['question']}),
#		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#
#	]
	#inlines = [ChoiceInline]
	#list_display = ('question', 'pub_date', 'was_published_recently')
	#list_filter = ['pub_date']
	#search_fields = ['question']