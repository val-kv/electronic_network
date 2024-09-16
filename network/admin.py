from django.contrib import admin
from .models import Supplier, NetworkNode, CustomUser


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'debt_to_supplier')
    list_filter = ('name',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)
        self.message_user(request, 'Задолженность очищена')


admin.site.register(Supplier)
admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(CustomUser)
