from django.db import models
from django.utils.html import mark_safe

class ProductCategory(models.Model):
    name=models.CharField(max_length=70)
    description=models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name=models.CharField(max_length=70)
    product_category=models.ForeignKey('ProductCategory',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)  # Optional for inventory tracking
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # For product images
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="100" />')
        return "No Image"

    image_tag.short_description = 'Image'

    def __str__(self):
        return f"{self.product_name}+{self.image}"


class Order(models.Model):
    customer_name = models.CharField(max_length=100, null=True, blank=True)  # Optional
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store price at the time of purchase
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.order
class Payment(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=[
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('online', 'Online')
    ])
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], default='pending')
    transaction_id = models.CharField(max_length=255, null=True, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.order
class Feedback(models.Model):
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 rating
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.comments
