from django.contrib import admin
from homepages.models import product, product_category, product_inventory, discount

# Register your models here.
admin.site.register(product)
admin.site.register(product_category)
admin.site.register(product_inventory)
admin.site.register(discount)
