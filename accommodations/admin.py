from django.contrib import admin
from .models import Region, Hotel, Address, Phone

admin.site.site_header = "Backend of tourism platform"
admin.site.site_title = "Admin panel of tourism platform"
admin.site.index_title = "Tourism management"

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    max_num = 1

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [AddressInline, PhoneInline]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Region)