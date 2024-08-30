from django.contrib import admin
from setup.models import User, UserProfile, Company

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Company)