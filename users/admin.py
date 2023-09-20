from django.contrib import admin
from users.models import ServiceClient, User


admin.site.register(User)

@admin.register(ServiceClient)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email', 'full_name',)

