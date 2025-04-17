from django.contrib import admin
from .models import Product
from django import forms

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'id': 'id_description',
                'style': 'white-space: pre-wrap; height: 300px; font-family: monospace;',
            }),
        }

    class Media:
        js = ('admin/description_template.js',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'description', 'price', 'is_available', 'is_brand_new', 'seller_location', 'created_at')
    list_filter = ('is_available', 'is_brand_new', 'seller_location')
    search_fields = ('name', 'seller_location', 'quality_description', 'image2', 'image3', 'image4', 'image5')
    ordering = ('-created_at',)

