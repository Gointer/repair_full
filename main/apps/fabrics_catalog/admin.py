from django.contrib import admin

from .models import FabricModel


class FabricAdmin(admin.ModelAdmin):
	list_display = ('name', 'type_of_fabric', 'description', )
	list_filter = ('name', 'type_of_fabric', )

admin.site.register(FabricModel, FabricAdmin)