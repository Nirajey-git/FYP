from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'username')
    readonly_feilds = ('date_joined', 'last_login')
    ordering = ('date_joined',)
    search_fields = ('email', 'username')

    filter_horizontal = ()
    list
admin.site.register(Account, AccountAdmin)
