from django.contrib import admin
from .models import CustomUser,MenteeProfile,MentorProfile
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(MentorProfile)
admin.site.register(MenteeProfile)