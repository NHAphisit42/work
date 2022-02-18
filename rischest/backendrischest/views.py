import io
from itertools import product
from unicodedata import category
from django.contrib import messages
from django.shortcuts import redirect, render
from homerischest.models import Register, Member, Package
from loginrischest.models import Category, Product, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.
@login_required(login_url='login_backend')
def home_backend(request):
    mb = Member.objects.all()
    mbcount = mb.count()
    return render(request, 'home_backend.html', {'mbcount':mbcount, 'mb':mb})

def table_backend(request):
    member = Member.objects.all()
    return render(request, 'table_backend.html', {'member':member})

def package(request):
    return render(request, 'add_package.html')

def table_package(request):
    package = Package.objects.all()
    return render(request, 'table_package.html', {'package':package})

def register_backend(request):
    return render(request, 'register_backend.html')

def login_backend(request):
    return render(request, 'login_backend.html')

def addcategory_backend(request):
    return render(request, 'addcategory_backend.html')

def categorytable(request):
    categories = Category.objects.all()
    return render(request, 'tablecategory.html', {'categories':categories})

def member_backend(request):
    member = Member.objects.all()
    return render(request, 'tablemember_backend.html', {'member':member})

def memberdetail(request, id):
    member = Member.objects.get(id=id)
    username =User.objects.all()
    return render(request, 'MemberDetail.html', {'member':member, 'username':username})

def chartdiagram(request):
    return render(request, 'chartdiagram.html')

def orderdetail(request, id):
    order = Member.objects.get(id=id)
    return render(request, 'OrderDetail.html', {'order':order})

def addmember_backend(request):
    return render(request, 'addmember_backend.html')

def addproduct_backend(request):
    categories = Category.objects.all()
    return render(request, 'addproduct_backend.html', {'categories':categories})

def tableproduct_backend(request): 
    products = Product.objects.all()
    return render(request, 'tableproduct_backend.html', {'products':products})

def productdeatil(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    return render(request, 'ProductDetail.html', {'product':product, 'categories':category})

def packagedetail(request, id):
    package = Package.objects.get(id=id)
    return render(request, 'PackageDetail.html', {'package':package})

def backend_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('home_backend')
    else:
        messages.Info(request, "ไม่พบข้อมูล")

def logout_BE(request):
    logout(request)
    return redirect('login_backend')
        
def remove_backend(request, id):
    member = Register.objects.get(id=id)
    member.delete()
    return redirect('table_backend')

def removeproduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('tableproduct')

def removeregister_backend(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('home_backend')

def removepackage(request, id):
    package = Package.objects.get(id=id)
    package.delete()
    return redirect('table_package')

def approve(request, status_id):
    status = Member.objects.get(id=status_id)
    status.status_member = True
    status.save()
    return redirect('home_backend')

def disapprove(request, status_id):
    status = Member.objects.get(id=status_id)
    status.status_member = False
    status.save()
    return redirect('home_backend')

# ฟังก์ชั่นข้อมูลต่าง ๆ
def adduser_backend(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        repassword=request.POST['repassword']
        email = request.POST['email']

        if username == "" or email == "" or password=="" or repassword=="" or first_name=="" or last_name=="":
            messages.info(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("register_backend")
        else:
            if password == repassword :
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username นี้มีคนใช้แล้ว")
                    return redirect("register_backend")
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"อีเมลนี้เคยลงทะเบียนไปแล้ว")
                    return redirect("register_backend")
                else:
                    user=User.objects.create_user(
                        username = username,
                        email=email,
                        password=password,
                        first_name = first_name,
                        last_name = last_name
                    )
                    user.save()
                    messages.info(request,"สร้างบัญชีเรียบร้อย")
                    return redirect("login_backend")
            else:
                messages.info(request,"ไม่สามารถลงทะเบียนได้รหัสผ่านไม่ตรงกัน")
                return redirect("register_backend")


def addproduct(request): 
    if request.method == 'POST' and request.FILES['product']:
        image = request.FILES['product']
        name = request.POST['name']
        category = request.POST['category']
        slug = request.POST['slug']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        
        fs = FileSystemStorage()
        img_url1 = "product/"+image.name
        filename = fs.save(img_url1, image)
        
        if name == "" or category == "" or description == "" or price == "" or stock == "" or slug == "" or image == "":
            messages.info(request,"กรุณาป้อนข้อมูลสินค้าให้ครบ")
            return redirect("addproduct_backend")
        else:
            product = Product.objects.create(
                name = name,
                category_id = category,
                description = description,
                price = price,
                slug = slug,
                stock = stock,
                image = img_url1
            )
            product.save()
            messages.info(request,"เพิ่มข้อมูลสินค้าเรียบร้อย")
            return redirect('addproduct_backend') 
        
def addmember(request): 
    if request.method == 'POST' and request.FILES['id_card'] and request.FILES['bankaccount']  and request.FILES['slip']:
        image_id_card = request.FILES['id_card']
        image_bank_account = request.FILES['bankaccount']
        image_slip = request.FILES['slip']
        gender = request.POST['gender']
        name = request.POST['name']
        phone = request.POST['phone']
        useremail = request.POST['useremail']
        package = request.POST['package']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        branch = request.POST['branch']
        recommender = request.POST['recommender']
        recommen = request.POST['recommen']
        bank = request.POST['bank']
        address = request.POST['address']
        zone = request.POST['zone']
        district = request.POST['district']
        province = request.POST['province']
        ZIP_code = request.POST['ZIP_code']

        fs = FileSystemStorage()
        img_url2 = "id_card/"+image_id_card.name
        filename = fs.save(img_url2, image_id_card)
        img_url3 = "bankaccount/"+image_bank_account.name
        filename = fs.save(img_url3, image_bank_account)
        img_url4 = "slip/"+image_slip.name
        filename = fs.save(img_url4, image_slip)

        if gender == "" or name == "" or phone == "" or useremail == "" or package == "" or accountname == "" or accountnumber == "" or branch == "" or recommender == "" or recommen == "" or bank == "" or address == "" or zone == "" or district == "" or province == "" or ZIP_code == "" :
            messages.info(request,"กรุณาป้อนข้อมูลสมาชิกให้ครบ") 
            return redirect("addmember_backend")
        else:
            member = Member.objects.create(
                gender = gender,
                name = name,
                phone = phone,
                useremail = useremail,
                package = package,
                accountname = accountname,
                accountnumber = accountnumber,
                branch = branch,
                recommender = recommender,
                recommen = recommen,
                bank = bank,
                address = address,
                zone = zone,
                district = district,
                province = province,
                ZIP_code = ZIP_code,
                image_id_card = img_url2,
                image_bank_account = img_url3,
                image_slip = img_url4,

            )
            member.save()
            messages.info(request,"เพิ่มข้อมูลสมาชิกเรียบร้อย")
            return redirect('addmember_backend') 
        

def insetpackage(request):
    if request.method == "POST" and request.FILES['image_package'] and request.FILES['image_package2']:
        name_package = request.POST['name_package']
        price_package = request.POST['price_package']
        bodytext = request.POST['bodytext']
        image_package = request.FILES['image_package']
        image_package2 = request.FILES['image_package2']
        
        fs = FileSystemStorage()
        img_url1 = "package/"+image_package.name
        filename = fs.save(img_url1, image_package)
        img_url2 = "package2/"+image_package2.name
        filename = fs.save(img_url2, image_package2)
        
        if name_package == "" or price_package == "" or bodytext == "" or img_url1 == "" or img_url2 == "":
            messages.info(request,"กรุณาป้อนข้อมูลแพ็คเกจให้ครบ")
        else:
            package = Package.objects.create(
                name_package = name_package,
                price_package = price_package,
                bodytext = bodytext,
                image_package = img_url1,
                image_package2 = img_url2
            )
            package.save()
            return redirect('table_package')
        

def updateproduct(request, id):
    try:
        if request.method == "POST":
            product = Product.objects.get(id=id)
            name = request.POST['name']
            category = request.POST['category']
            slug = request.POST['slug']
            description = request.POST['description']
            price = request.POST['price']
            stock = request.POST['stock']
            
            product.name = name
            product.category_id = category
            product.slug = slug
            product.description = description
            product.price = price
            product.stock = stock
            product.save()
            
            if request.FILES['product']:
                image = request.FILES['product']
                fs = FileSystemStorage()
                img_url1 = "product/"+image.name
                filename = fs.save(img_url1, image)
                product.image = img_url1
                product.save()
            
            messages.info(request,"แก้ไขข้อมูลสินค้าเรียบร้อย")
            return redirect('tableproduct')
    except:
        return redirect('tableproduct')
    
def updatepackage(request, id):
    try:
        if request.method == "POST":
            package = Package.objects.get(id=id)
            name_package = request.POST['name_package']
            bodytext = request.POST['bodytext']
            price_package = request.POST['price_package']
            
            package.name_package = name_package
            package.bodytext = bodytext
            package.price_package = price_package
            package.save()
            
            if request.FILES['image_package'] and request.FILES['image_package2']:
                image_package = request.FILES['image_package']
                image_package2 = request.FILES['image_package2']
                fs = FileSystemStorage()
                
                img_url1 = "package/"+image_package.name
                filename = fs.save(img_url1, image_package)
                img_url2 = "package2/"+image_package2.name
                filename = fs.save(img_url2, image_package2)
                
                package.image_package = img_url1
                package.image_package2 = img_url2
                package.save()
            return redirect('table_package')
    except:
        return redirect('table_package')
    
def addcategory(request):
    if request.method == "POST" and request.FILES == ['img']:
        name = request.POST['name']
        slug = request.POST['slug']
        img = request.FILES['img']
        
        fs = FileSystemStorage()
        img_url = "category_img/"+img.name
        filename = fs.save(img_url, img)
        
        if name == "" or slug == "" or img_url == "":
            messages.info(request,"กรุณาป้อนข้อมูลหมวดหมู่ให้ครบ")
        else:
            category = Category.objects.create(
                name = name,
                slug = slug,
                img = img_url
            )
            category.save()
            return redirect('addproduct_backend')