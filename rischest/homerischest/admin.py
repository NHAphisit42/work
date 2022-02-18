from django.contrib import admin
from homerischest.models import Member, Register, Recommender, Package, Base, Slideshow
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    
class RegisterDesign(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'package', 'address', 'zone', 'district', 'province', 'ZIP_code', 'choose_delivery', 'total_delivery', 'Date')
    
class Slideshowdesign(admin.ModelAdmin):
    list_display = ('id', 'img', 'name_img')
    
admin.site.register(Member)
admin.site.register(Register, RegisterDesign)
admin.site.register(Recommender)
admin.site.register(Package, SomeModelAdmin)
admin.site.register(Base, SomeModelAdmin)
admin.site.register(Slideshow, Slideshowdesign)