from django.contrib import admin
from .models import Product, StatusManagement, CategoryManagement, ColorManagement, BrandManagement

# Register your models here.
admin.site.register(Product)
admin.site.register(StatusManagement)
admin.site.register(CategoryManagement)
admin.site.register(ColorManagement)
admin.site.register(BrandManagement)