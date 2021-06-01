from django.contrib import admin
from appcom.models import Customerdb
from appcom.models import Task

# Register your models here.
#admin.site.register(Customerdb)

#@admin.register(Customerdb)
class CustomerdbAdmin(admin.ModelAdmin):
	list_display = ('cuid', 'cuname', 'cumail','pubdate')
	#list_editable = ('cuname',)
	list_filter = ('cuid', 'cuname')
	search_fields = ('cuname',)
	#fields = (
		#'cuid', 
	   # 'cuname',
	   # 'cumail', 
	    #'cupass', 
	    #'Discription', 
	 #   'pubdate' 
	#)



	fieldsets = (
		(None, {
			'fields':(
				'cuid', 
				'cuname',
				'cumail',
				'cupass', 
				'Discription', 
				'pubdate'
				)		
		}),
	)
admin.site.register(Customerdb,CustomerdbAdmin)

admin.site.register(Task)
  

