from django.contrib import admin
from .models import *

admin.site.register(CheapPackages)
admin.site.register(LuxuryPackages)
admin.site.register(CampingPackages)

from django.contrib import admin
from .models import *

admin.site.register(Newsletter)
admin.site.register(ContactUs)