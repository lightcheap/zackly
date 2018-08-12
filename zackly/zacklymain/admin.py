from django.contrib import admin
from .models import Income, FixedCost, SpFixedCost

# Register your models here.
admin.site.register(Income)
admin.site.register(FixedCost)
admin.site.register(SpFixedCost)