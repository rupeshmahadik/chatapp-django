from django.contrib import admin

# Register your models here.

from models import chatter

class chatterAdmin(admin.ModelAdmin):
	list_display = ['chat_field']


	class Meta:
		model = chatter

admin.site.register(chatter , chatterAdmin)