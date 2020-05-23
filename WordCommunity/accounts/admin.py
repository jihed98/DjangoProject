from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile

'''
abbiamo registrato il nostro modello UserProfile
'''
admin.site.register(UserProfile)