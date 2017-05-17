from django.contrib import admin

# Register your models here.
from .models import Posts 

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["timestamp"]
	list_editable = ["title"]
	list_filter = [ "updated", "timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Posts

admin.site.register(Posts, PostModelAdmin)
