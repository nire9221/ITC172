from django.contrib import admin
from .models import ProductType, Product, Review, Genre, Article, Job, Event

# Register models
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Article)
admin.site.register(Job)
admin.site.register(Event)