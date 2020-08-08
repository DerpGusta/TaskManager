from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import (KRA,
                     Metric,
                     Task,
                     Department,
                     Branch,
                     UserData)
# from django.contrib.auth.models import Use

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserDataInline(admin.TabularInline):
    model = UserData
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserDataInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(KRA)
# admin.site.register(UserData)
admin.site.register(Metric)
admin.site.register(Task)
admin.site.register(Department)
admin.site.register(Branch)

# Register your models here.
