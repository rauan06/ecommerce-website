from django.db import models

class product_category(models.Model):
    """Category description"""
    name = models.CharField(max_length=50, unique=True)

    """Category changes dates"""
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now_add = True)
    deleted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Product_categories'


class product(models.Model):
    """Products description"""
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='homepages/static/images')

    categories = models.ManyToManyField(product_category)
    
    """Product changes dates"""
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now_add = True)
    deleted_at = models.DateTimeField(auto_now_add = True)

    """Product Rels"""
    
    def __str__(self):
        return self.name[:50] + ' ...'


class discount(models.Model):
    """Dicount description"""
    product_name = models.ForeignKey(product, on_delete=models.CASCADE)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField()

    """Discount changes dates"""
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now_add = True)
    deleted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.discount_percent) + "%" + "  -  " + self.product_name.name
    

class product_inventory(models.Model):
    """Inventory description"""
    product_name = models.OneToOneField(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    """Inventory changes dates"""
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now_add = True)
    deleted_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'Product inventories'

    def __str__(self):
        return str(self.quantity) + " - " + self.product_name.name