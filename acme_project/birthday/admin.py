from django.contrib import admin

from .models import Birthday, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
    )


admin.site.register(Birthday)
admin.site.register(Tag, TagAdmin)
