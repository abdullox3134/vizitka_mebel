from django.contrib import admin

from home.models import Home, About, Gallery, Versions, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'created_at')
    search_fields = ('name', 'phone', 'message')
    list_filter = ('phone',)

    def has_add_permission(self, request):
        return False  # Disable the ability to add new contacts via the admin panel

    def has_change_permission(self, request, obj=None):
        return False  # Disable the ability to change existing contacts via the admin panel


admin.site.register(Home)
admin.site.register(About)
admin.site.register(Gallery)
admin.site.register(Versions)
