from django.contrib import admin

# Register your models here.
from .models import Files 


class FilesModelAdmin(admin.ModelAdmin):
	list_display = ["imagen", "timestamp"]
	list_display_links = ["imagen"]
	#list_editable = ["imagen"]
	list_filter = [ "timestamp"]

	search_fields = ["imagen", "timestamp"]
	class Meta:
		model = Files



admin.site.register(Files, FilesModelAdmin)