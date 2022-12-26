from django.contrib import admin
from .models import *

# Register your models here.

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ["name", "phone"]


admin.site.register(PersonalInformation)
admin.site.register(About)
admin.site.register(Projects)
admin.site.register(Skills)