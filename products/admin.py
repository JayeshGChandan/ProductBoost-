from django.contrib import admin

# Register your models here.
from .models import Product, Vote, Reply

admin.site.register(Product)
admin.site.register(Vote)
admin.site.register(Reply)
