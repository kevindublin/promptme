from django.contrib import admin
from .models import Draft, Feedback

# Register your models here.
@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):

    def __str__(self):
        return self.text


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass
