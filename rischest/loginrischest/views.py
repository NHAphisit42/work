from email import message
from django.shortcuts import render, get_object_or_404
from loginrischest.models import Category, Product, Cart, CartItem, Order, OrderItem, Announce, Income, Income_team
from homerischest.models import Member, Slideshow
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# from django.utils import json as simplejson
from json import dumps

# Create your views here.
def home_richest(request, category_slug=None):
    # product = Product.objects.all()
    slide = Slideshow.objects.all()
    announce = Announce.objects.all()
    product=None
    category_page=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        product=Product.objects.all().filter(category=category_page,available=True)
    else :
        product=Product.objects.all().filter(available=True)
    
    #12 / 3 = 4
    paginator=Paginator(product,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        productperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        productperPage=paginator.page(paginator.num_pages)
        
    return render(request, 'home_richest.html', {'product':productperPage, 'announce':announce, 'category':category_page, 'slide':slide})

def home_proflie(request):
    return render(request, 'home_proflie.html')

def home_connect(request):
    return render(request, 'connect.html')
   
def Order_History(request):
    return render(request, 'Order_History.html')

def home_sale(request):
    sale = Income.objects.all()
    sale_team = Income_team.objects.all()
    return render(request, 'home_sale.html', {'sale':sale, 'sale_team':sale_team})

def home_recommend(request):
    return render(request, 'home_recommend.html')

def home_point(request):
    return render(request, 'home_point.html')

def home_bonus(request):
    return render(request, 'home_bonus.html')

def detail_order(request):
    return render(request, 'detail_order.html')

def logout_backend(request):
    logout(request)
    return redirect('login')

def detail_announce(request, id):
    announce = Announce.objects.get(id=id)
    return render(request, 'detail-announce.html', {'announce':announce})
     
def home_product(request, category_slug=None):
    product=None
    category_page=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        product=Product.objects.all().filter(category=category_page,available=True)
    else :
        product=Product.objects.all().filter(available=True)
    
    paginator=Paginator(product,8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        productperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        productperPage=paginator.page(paginator.num_pages)
    return render(request, 'home_product.html', {'product':productperPage, 'categories':category_page})

def detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Exception as e:
        raise e
    return render(request, 'detail-product.html', {'product':product})

def category_detail(request, slug):
    if(Category.objects.filter(slug=slug)):
        category = Category.objects.all()
        product = Product.objects.filter(category=category.get(slug=slug))
        return render(request, 'category-detail.html', {'product':product})
    else:
        message.info(request, 'ไม่มีหมวดหมู่นี้')
        return redirect('product_by_category')

def searchproduct(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        product = Product.objects.filter(name__icontains=q)
        return render(request, 'searchProduct.html', {'product':product})
    else:
        return render(request, 'home_product.html')

def cartdetail(request):
    total=0
    counter=0
    cart_items=None
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request)) #ดึงตะกร้า
        cart_items=CartItem.objects.filter(cart=cart,active=True) #ดึงข้อมูลสินค้าในตะกร้า
        for item in cart_items:
            total+=(item.product.price*item.quantity)
            counter+=item.quantity
    except Exception as e :
        pass
    
    return render(request, 'cartdetail.html', {'cart_items':cart_items, 'total':total, 'counter':counter})

def updatecart(request, id):
    if request.method=='POST':
        quantity=int(request.POST.get('quantity'))
        cart_item=CartItem.objects.get(id=id)
        cart_item.quantity=quantity
        cart_item.save()
        return redirect('cartdetail')

   
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def addCart(request, product_id):
    #ดึงสินค้าที่เราซื้อมาใช้งาน
    product=Product.objects.get(id=product_id)
    #สร้างตะกร้าสินค้า
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
        
    try:
        #ซื้อรายการสินค้าซ้ำ
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity<cart_item.product.stock :
            #เปลี่ยนจำนวนรายการสินค้า
            cart_item.quantity+=1
            #บันทึก/อัพเดทค่า
            cart_item.save()
    except CartItem.DoesNotExist:
        #ซื้อรายการสินค้าครั้งแรก
        #บันทึกลงฐานข้อมูล
        cart_item=CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()
    return redirect('cartdetail')

def removeCart(request, product_id):
    #ทำงานกับตะกร้าสินค้า A
    cart=Cart.objects.get(cart_id=_cart_id(request))
    #ทำงานกับสินค้าที่จะลบ 1
    product=get_object_or_404(Product, id=product_id)
    cartItem=CartItem.objects.get(product=product, cart=cart)
    #ลบรายการสินค้า 1 ออกจากตะกร้า A โดยลบจาก รายการสินค้าในตะกร้า (CartItem)
    cartItem.delete()
    return redirect('cartdetail')

# Update Profiles User Model
def update_profile(request, id):
    # update profile
    if request.method == 'POST':
        address = request.POST['address']
        phone = request.POST['phone']
        usermail = request.POST['usermail']
        zone = request.POST['zone']
        district = request.POST['district']
        province = request.POST['province']
        ZIP_code = request.POST['ZIP_code']
        
        member = Member.objects.get(id=id)
        member.address = address
        member.phone = phone
        member.usermail = usermail
        member.zone = zone
        member.district = district
        member.province = province
        member.ZIP_code = ZIP_code
        
        member.save()
        return redirect('home_proflie')
    else:
        return render(request, 'home_proflie.html')
    
def order(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        zone = request.POST['zone']
        district = request.POST['district']
        province = request.POST['province']
        post_code = request.POST['post_code']
        total = request.POST['total']
        
        if name == "" and phone == "" and address == "" and zone == "" and district == "" and province == "" and post_code == "" and total == "" :
            message.info(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
        else:
            addorder = Order.objects.create(
                name = name,
                phone = phone,
                address = address,
                zone = zone,
                district = district,
                province = province,
                post_code = post_code,
                total = total
            )
            addorder.save()
            return redirect('detail_order')