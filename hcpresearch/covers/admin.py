from django.contrib import admin
from .models import Covers


# Register your models here.

class CoverInline(admin.TabularInline):
    model = Covers


class CoversAdmin(admin.ModelAdmin):
    inline = CoverInline


admin.site.register(Covers, CoversAdmin)
