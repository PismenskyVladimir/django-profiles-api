from django.contrib import admin

from profiles_api.models import (
    ProfileFeedItem,
    UserProfile,
)


admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
