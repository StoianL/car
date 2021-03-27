from django.contrib import admin
from car.models import Car, Manifactures, Owner, Parts, Repair, Works

# Register your models here.
admin.site.register(Car)
admin.site.register(Manifactures)
admin.site.register(Owner)
admin.site.register(Parts)
admin.site.register(Repair)
admin.site.register(Works)
