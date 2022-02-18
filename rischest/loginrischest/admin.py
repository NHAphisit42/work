from django.contrib import admin
from loginrischest.models import Category, Product, Cart, CartItem, Order, OrderItem, Announce, Income, Income_team
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    
class IcomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'income', 'datetime']  
    
class Icome_teamAdmin(admin.ModelAdmin):
    list_display = ['id', 'team_name', 'income', 'date']  
  
admin.site.register(Category)
admin.site.register(Product, SomeModelAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Announce, SomeModelAdmin)
admin.site.register(Income, IcomeAdmin)
admin.site.register(Income_team, Icome_teamAdmin)