from django.contrib import admin


# Register your models here.
from .models import *


class newsletteradmin(admin.ModelAdmin):

 admin.site.register(NewsLetterUser)
 admin.site.register(intrest)