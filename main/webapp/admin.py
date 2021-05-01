from django.contrib import admin
from webapp.models import Category, Review, Product
# Register your models here.


admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Product)