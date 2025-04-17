
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    image4 = models.ImageField(upload_to='products/', null=True, blank=True)
    image5 = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    is_brand_new = models.BooleanField(default=True)
    quality_description = models.TextField(blank=True)
    seller_whatsapp = models.CharField(max_length=15)
    seller_instagram = models.CharField(max_length=50, blank=True)
    seller_phone = models.CharField(max_length=15, blank=True)
    seller_email = models.EmailField(blank=True)
    delivery_cost = models.CharField(max_length=50)
    delivery_location = models.CharField(max_length=100)
    delivery_method = models.CharField(max_length=100)
    seller_location = models.CharField(max_length=100)
    is_negotiable = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_weekly_offer = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[str(self.pk)])
    

    def __str__(self):
        return self.name
    



    
class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=5)  # 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.name}"


    