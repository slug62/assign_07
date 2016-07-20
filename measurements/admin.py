from django.contrib import admin
from .models import Area, Location, Category, Measurement


class LocationInline(admin.StackedInline):
    model = Location
    extra = 1

class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1

class AreaAdmin(admin.ModelAdmin):
    inlines = [
        LocationInline
    ]

class LocationAdmin(admin.ModelAdmin):
    inlines = [
        MeasurementInline
    ]

class CategoryAdmin(admin.ModelAdmin):
    fields = ['id', ]
    filter_vertical = ['members']

admin.site.register(Area, AreaAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
