from django.contrib import admin
from apps.accounts.models import User, UserPrompt

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPrompt)
class UserPromptAdmin(admin.ModelAdmin):
    pass
