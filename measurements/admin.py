from django.contrib import admin
from .models import Area, Location, Category

admin.site.register(Area)
admin.site.register(Location)
admin.site.register(Category)

# class LocationInline(admin.TabularInline):
#     model = Location
#
# class AreaAdmin(admin.ModelAdmin):
#     inlines = [
#         LocationInline
#     ]
#
