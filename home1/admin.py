from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin.sites import site
from home1.models import about,Contact
from home1.models import iceCream,carousel


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display=("name","designation","image","description","email")
admin.site.register(about,AboutAdmin)

class iceCreamAdmin(admin.ModelAdmin):
   list_display=('flavour','size','price','offer_price','icecream_photo','description')
admin.site.register(iceCream,iceCreamAdmin)

class  carouselAdmin(admin.ModelAdmin):
    list_display = ("name","image","description")
admin.site.register(carousel,carouselAdmin)

# class  ContactAdmin(admin.ModelAdmin):
#     list_display = ("first_name","last_name","Country","Message")
admin.site.register(Contact)
