from django.contrib import admin
from .models import Region

admin.site.site_header = "Backend of tourism platform"
admin.site.site_title = "Admin panel of tourism platform"
admin.site.index_title = "Tourism management"

admin.site.register(Region)
