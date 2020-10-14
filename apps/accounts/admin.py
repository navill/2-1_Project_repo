from django.contrib import admin

from django.contrib.auth.hashers import check_password, make_password

from accounts.models import AdminUser, NormalUser


def validate_password(user, form, obj):
    if user:
        user_password = user[0].password
        if not (check_password(form.data['password'], user_password) or user_password ==
                form.data['password']):
            obj.password = make_password(obj.password)
        else:
            obj.password = user_password
    else:
        obj.password = make_password(obj.password)
    return obj


class AdminUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'password', 'is_active', 'is_admin']
    list_display = ['username', 'email', 'last_login', 'date_joined']

    def save_model(self, request, obj, form, change):
        user = AdminUser.objects.filter(pk=obj.pk)
        obj = validate_password(user, form, obj)
        super().save_model(request, obj, form, change)


admin.site.register(AdminUser, AdminUserAdmin)


class NormalUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'password', 'is_active']
    list_display = ['username', 'email', 'last_login', 'date_joined']

    def save_model(self, request, obj, form, change):
        user = NormalUser.objects.filter(pk=obj.pk)
        obj = validate_password(user, form, obj)
        super().save_model(request, obj, form, change)


admin.site.register(NormalUser, NormalUserAdmin)
