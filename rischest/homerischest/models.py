from re import M
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  Register(models.Model):
    package_CHOICE=(
        ('Diamond', 'Diamond'), ('Silver','Silver'), ('VIP','VIP'),
    )

    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=10) #เบอร์โทรศัพท์
    package = models.CharField(max_length=255, choices=package_CHOICE, null=True)
    address = models.TextField(null=True)
    zone = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    ZIP_code = models.CharField(max_length=5, null=True)
    choose_delivery = models.CharField(max_length=255, null=True)
    total_delivery = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'address'
        managed = True
        verbose_name = 'ที่อยู่จัดส่ง'
        verbose_name_plural = 'ที่อยู่จัดส่ง'

    def __str__(self):
        return self.name
    
class Member(models.Model):
    gender_CHOICE=(
        ('นาย','นาย'), ('นางสาว','นางสาว'), ('นาง','นาง'),
    )

    BANK_CHOICE =(('ธนาคารกรุงเทพ','ธนาคารกรุงเทพ'), ('ธนาคารกรุงไทย','ธนาคารกรุงไทย'),
        ('ธนาคารกรุงศรีอยุธยา','ธนาคารกรุงศรีอยุธยา'), ('ธนาคารกสิกรไทย','ธนาคารกสิกรไทย'),
        ('ธนาคารเกียรตินาคินภัทร','ธนาคารเกียรตินาคินภัทร'), ('ธนาคารทหารไทยธนชาต','ธนาคารทหารไทยธนชาต'),
        ('ธนาคารไทยพาณิชย์','ธนาคารไทยพาณิชย์'), ('ธนาคารยูโอบี','ธนาคารยูโอบี'),
        ('ธนาคารอิสลามแห่งประเทศไทย','ธนาคารอิสลามแห่งประเทศไทย'), ('ธนาคารออมสิน','ธนาคารออมสิน'),
    )

    BOOLMEMER_CHOICES=(
        (None, 'รอการอนุมัติ'), (True, 'อนุมัติ'), (False, 'ไม่อนุมัติ'),
    )

    package_CHOICE=(
        ('Diamond', 'Diamond'), ('Silver','Silver'), ('VIP','VIP'),
    )

    package_CHOICE=(
        ('Diamond', 'Diamond'), ('Silver','Silver'), ('VIP','VIP'),
    )
    
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #เชื่อมความสัมพันธ์ตารางระหว่าง Member กีบ User ในการล็อกอิน 
    gender = models.CharField(max_length=100, choices=gender_CHOICE, null=True)
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=10) #เบอร์โทรศัพท์
    useremail = models.CharField(max_length=255, null=True)
    package = models.CharField(max_length=255, choices=package_CHOICE, null=True)
    accountname = models.CharField(max_length=255) #ชื่อบัญชี
    accountnumber = models.CharField(max_length=100) #เลขบัญชี
    branch = models.CharField(max_length=255, null=True) #สาขาของธนาคาร
    recommender = models.CharField(max_length=255, null=True) #รหัสผู้แนะนำ
    recommen = models.CharField(max_length=255, null=True) #ชื่อผู้แนะนำ
    bank = models.CharField(max_length=255, choices=BANK_CHOICE, null=True) #ชื่อธนาคาร
    image_id_card = models.FileField(upload_to="id_card", blank=True) #เก็บรูปบัตรประชาชน
    image_bank_account = models.FileField(upload_to="bankaccount", blank=True) #เก็บรูปสมุดธนาคาร
    image_slip = models.FileField(upload_to="slip", blank=True) #เก็บรูปสลิปการโอน
    date = models.DateTimeField(auto_now_add=True, null=True) #วันที่สมัคร
    status_member = models.BooleanField(null=True, default=None, choices=BOOLMEMER_CHOICES)
    address = models.TextField(null=True)
    zone = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    ZIP_code = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = 'member'
        managed = True
        verbose_name = 'สมาชิก'
        verbose_name_plural = 'ข้อมูลสมาชิก'

    def __str__(self):
        return self.name
    
#ตารางฐานข้อมูลผู้แนะนำสมาชิก
class Recommender(models.Model):
    gender_CHOICE=(
        ('นาย','นาย'),
        ('นางสาว','นางสาว'),
        ('นาง','นาง'),
    )
    BOOL_CHOICES=(
        (None, 'รอการอนุมัติ'),
        (True, 'อนุมัติ'), 
        (False, 'ไม่อนุมัติ'),
    )

    user = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=100, choices=gender_CHOICE, null=True)
    name = models.CharField(max_length=255, unique=True)
    tel = models.CharField(max_length=20, null=True)
    status = models.BooleanField(null=True, default=None, choices=BOOL_CHOICES)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ชื่อ'
        verbose_name_plural = 'ผู้แนะนำ'

    def __str__(self):
        return self.name
    
class Package(models.Model):
    image_package = models.FileField(upload_to="package", blank=True)
    image_package2 = models.FileField(upload_to="package2", blank=True, null=True)
    name_package = models.CharField(max_length=255, null=True)
    price_package = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bodytext = models.TextField(null=True)
    
    class Meta:
        db_table = 'Package'
        managed = True
        verbose_name = 'แพคเกจ'
        verbose_name_plural = 'ข้อมูลแพคเกจ'
        
    def __str__(self):
        return self.name_package
    
class Base(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    
    class Meta:
        db_table = 'Base'
        managed = True
        verbose_name = 'ข้อมูลหลัก'
        verbose_name_plural = 'ข้อมูลหลัก'
        
    def __str__(self):
        return self.title
    
class Slideshow(models.Model):
    img = models.FileField(upload_to="slideshow", blank=True)
    name_img = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name_img
    
    class Meta:
        db_table = 'Slideshow'
        managed = True
        verbose_name = 'สไลด์โชว์'
        verbose_name_plural = 'ข้อมูลสไลด์โชว์'