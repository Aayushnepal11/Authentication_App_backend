from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


admin.site.site_title="Authentication"
admin.site.site_header="Authentication"


class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name", "email", "password1", 
                "password2", "gender", "is_staff",
                "is_active", "groups", "user_permissions" 
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email", )



admin.site.register(User, CustomAdmin)