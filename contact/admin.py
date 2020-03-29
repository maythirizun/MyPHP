from django.contrib import admin
from .models import Mitsumori, ServiceGroup, Service, MitsumoriService, Departmet

class MitsumoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'request_no', 'name', 'message', 'create_date', 'update_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'message', 'create_date', 'update_date')
    list_per_page = 20

class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 20

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service_group')
    list_display_links = ('name', 'service_group')
    search_fields = ('name', 'service_group')
    list_per_page = 20

class MitsumoriServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'mitsumori', 'service', 'service_group')
    search_fields = ('mitsumori', 'service', 'service_group')
    list_per_page = 20

class DepartmetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

# class Mitsumori_DetailsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'message', 'm_file', 'create_date', 'update_date')
#     search_fields = ('name', 'message')
#     list_per_page = 20

admin.site.register(Mitsumori, MitsumoriAdmin)
admin.site.register(ServiceGroup, ServiceGroupAdmin)
admin.site.register(Service, ServiceGroupAdmin)
admin.site.register(MitsumoriService, MitsumoriServiceAdmin)
admin.site.register(Departmet, DepartmetAdmin)
# admin.site.register(Mitsumori_Details, Mitsumori_DetailsAdmin)
