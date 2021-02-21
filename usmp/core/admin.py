from django.contrib import admin

from .models import Core


class CoreAdmin(admin.ModelAdmin):
    """ This is the Core of our app. """

    pass


admin.site.register(Core, CoreAdmin)
