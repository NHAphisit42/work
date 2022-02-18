from tabnanny import verbose
from django.db import models
from homerischest.models import Member
from django.contrib.auth.models import User
from django.core import serializers

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    img = models.FileField(upload_to='category_img', blank=True)
    
    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'หมวดหมู่'
        verbose_name_plural = 'หมวดหมู่สินค้า'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True) #ชื่อสินค้า
    slug = models.SlugField(max_length=255,unique=True, null=True)
    description = models.TextField(blank=True) #คำอธิบายสินค้า
    price = models.DecimalField(max_digits=10, decimal_places=2) #ราคาสินค้า
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #หมวดหมู่สินค้า
    image = models.FileField(upload_to="product", blank=True) #รูปภาพสินค้า
    stock = models.IntegerField() #จำนวนสินค้า
    available = models.BooleanField(default=True) #สถานะ
    created = models.DateTimeField(auto_now_add=True) #วันเพิ่มสินค้า
    update = models.DateTimeField(auto_now=True) #วันอัพเดตสินค้า
    
    class Meta:
        db_table = 'Product'
        managed = True
        verbose_name = 'ตะกร้าสินค้า'
        verbose_name_plural = 'ข้อมูลสินค้า'

    def __str__(self):
        return self.name

# ฐานข้อูมูลตะกร้าสินค้า
class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        db_table = 'cart'
        ordering = ('date_add',)
        verbose_name = 'ตะกร้าสินค้า'
        verbose_name_plural = 'ข้อมูลตะกร้าสินค้า'

# ฐานข้อูมูลสินค้าในตะกร้า
class CartItem(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'cartitem'
        verbose_name = 'รายการในตะกร้า'
        verbose_name_plural = 'ข้อมูลรายการในตะกร้าสินค้า'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

# ฐานข้อมูลออเดอร์
class Order(models.Model):
    รอการจัดส่ง = 0 
    อยู่ระหว่างการจัดส่ง = 1
    จัดส่งสำเร็จ = 2
    จัดส่งไม่สำเร็จ = 3
    ยกเลิกการจัดส่ง = 4
    
    order_CHOICE=(
       (รอการจัดส่ง,'รอการจัดส่ง'), (อยู่ระหว่างการจัดส่ง, 'อยู่ระหว่างการจัดส่ง'), (จัดส่งสำเร็จ,'จัดส่งสำเร็จ'), (จัดส่งไม่สำเร็จ,'จัดส่งไม่สำเร็จ'), (ยกเลิกการจัดส่ง,'ยกเลิกการจัดส่ง')
    )
    
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255,blank=True, null=True)
    phone = models.CharField(max_length=10, null=True) #เบอร์โทรศัพท์
    address = models.TextField(null=True)
    zone = models.CharField(max_length=255,blank=True, null=True)
    district = models.CharField(max_length=255,blank=True, null=True)
    province = models.CharField(max_length=255,blank=True, null=True)
    post_code = models.CharField(max_length=5,blank=True, null=True)
    choose_delivery = models.CharField(max_length=255,blank=True, null=True)
    total = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    status_order = models.PositiveIntegerField(choices=order_CHOICE, default=0)

    class Meta :
        db_table='Order'
        ordering=('id',)
        verbose_name = 'การสั่งซื้อ'
        verbose_name_plural = 'ข้อมูลการสั่งซื้อ'

    def __str__(self):
        return str(self.id)

# ข้อมูลรายละเอียดออเดอร์
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    cart = models.ManyToManyField(CartItem)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta :
        db_table='OrderItem'
        ordering=('order',)
        verbose_name = 'รายละเอียดออเดอร์'
        verbose_name_plural = 'ข้อมูลรายละเอียดออเดอร์'

    def sub_total(self):
        return self.quantity*self.price
    
    def __str__(self):
        return self.product
    
#ประชาสัมพันธ์
class Announce(models.Model):
    name = models.CharField(max_length=255, unique=True) #ชื่อสินค้า
    description = models.TextField(blank=True) #คำอธิบายสินค้า
    image = models.FileField(upload_to="announce", blank=True) #รูปภาพสินค้า    
    created = models.DateTimeField(auto_now_add=True) #วันเพิ่มสินค้า
    update = models.DateTimeField(auto_now=True) #วันอัพเดตสินค้า
    
    class Meta:
        db_table = 'Announce'
        managed = True
        verbose_name = 'ประชาสัมพันธ์'
        verbose_name_plural = 'ประกาศประชาสัมพันธ์'

    def __str__(self):
        return self.name
    
class Income(models.Model): 
    name = models.CharField(max_length=255, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    datetime = models.DateField() 
    
    def __str__(self):
        return self.name
    
    def total(self):
        return self.income
    
    class Meta:
        db_table = 'income'
        managed = True
        verbose_name = 'ยอดขาย'
        verbose_name_plural = 'ข้อมูลยอดขาย'
        
class Income_team(models.Model):
    team_name = models.CharField(max_length=255, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateField()
    
    def __str__(self):
        return self.team_name
    
    class Meta:
        db_table = 'income_team'
        managed = True
        verbose_name = 'ยอดขายทีม'
        verbose_name_plural = 'ข้อมูลยอดขายทีม'