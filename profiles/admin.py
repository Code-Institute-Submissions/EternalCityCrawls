from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_full_name',
        'default_phone_number',
        'default_town_or_city',
        'default_street_address1',
        'default_county',
        'default_postcode',
        'default_country',

    )

    ordering = ('user',)



admin.site.register(UserProfile, UserProfileAdmin)
