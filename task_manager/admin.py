from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "photo")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position", "photo")}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                        "photo",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = (
        "is_completed",
        "priority",
    )


admin.site.register(TaskType)
admin.site.register(Position)
