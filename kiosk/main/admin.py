from django.contrib import admin
from django.utils.html import format_html
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock_quantity', 'is_active', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:100px; height:100px;" />', obj.image.url)
        return "No Image"
    image_preview.allow_tags = True

admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Feedback)



