from django.contrib import admin

from .models import Contact,Product,OwnedProduct,Interaction,Channel

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(OwnedProduct)
admin.site.register(Interaction)
admin.site.register(Channel)