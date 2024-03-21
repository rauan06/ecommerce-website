from django.contrib import admin
from homepages.models import product, product_category, product_inventory, discount

class productAdmin(admin.ModelAdmin):
    filter_horizontal = ['categories']


# Register your models here.
admin.site.register(product, productAdmin)
admin.site.register(product_category)
admin.site.register(product_inventory)
admin.site.register(discount)