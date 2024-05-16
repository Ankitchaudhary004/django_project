from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin.sites import site
from home1.models import about
from home1.models import iceCream

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","subject")
admin.site.register(about,AboutAdmin)

class iceCreamAdmin(admin.ModelAdmin):
   list_display=('flavour','size','price','offer_price','icecream_photo','description')
admin.site.register(iceCream,iceCreamAdmin)