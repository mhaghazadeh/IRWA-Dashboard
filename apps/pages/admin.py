from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Inventory)
admin.site.register(WasteType)
admin.site.register(WasteState)
admin.site.register(WasteClass)
admin.site.register(ContainerType)
admin.site.register(Site)
admin.site.register(Facility)
admin.site.register(OriginFacility)
admin.site.register(Radionuclide)
admin.site.register(Material)
admin.site.register(FieldRule)