from django.contrib import admin
from .models import Profession
from .models import Career
from .models import CareerProfs

# Register your models here.


admin.site.register(Profession)
admin.site.register(Career)
admin.site.register(CareerProfs)