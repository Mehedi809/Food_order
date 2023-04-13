from django.contrib import admin
from .models import custommer, product, order

# Register your models here.
class custommeradmin(admin.ModelAdmin):
    search_fields = ['email', 'phone']
    list_filter = ['phone', 'name']
    list_display = ['name', 'email', 'phone']
    list_per_page = 10

class productadmin(admin.ModelAdmin):
    search_fields = ['name', 'category']
    list_filter = ['date_created', 'price']
    list_display = ['name', 'price', 'category']
    list_per_page = 10

class orderadmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(custommer, custommeradmin)
admin.site.register(product, productadmin)
admin.site.register(order, orderadmin)