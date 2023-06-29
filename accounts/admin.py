from django.contrib import admin
from .models import *



class ProfileDisplayImagesStacked(admin.StackedInline):
    model = ProfileDisplayImages

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileDisplayImagesStacked]

    class Meta:
        model = User

  


admin.site.register(User, UserAdmin)
admin.site.register(Vendor)
admin.site.register(ProfileDisplayImages)
admin.site.register(Reception)
