from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Music)
admin.site.register(PlayListe)
admin.site.register(Mix)
admin.site.register(UserProfile)
# Register your models here.