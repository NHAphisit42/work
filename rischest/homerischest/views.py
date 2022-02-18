from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from homerischest.models import Register, Member, Package, Base, Slideshow
from loginrischest.models import Product
from django.contrib.auth import authenticate, login as auth_login
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from PIL import Image
from json import dumps

# Create your views here.
# ฟังก์ชันหน้าแรก
def home(request):
    package = Package.objects.all()
    base = Base.objects.all()
    products = Product.objects.all()
    slide = Slideshow.objects.all()
    paginator = Paginator(products, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
        
    try:
        productpage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        productpage = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'package':package, 'base':base, 'products':productpage, 'slide':slide})

# หน้าฟอร์มRegister
def register(request):
    package = Package.objects.all()
    products = Product.objects.all()
    return render(request, 'register.html', {'package':package, 'products':products})

# หน้าฟอร์มlogin
def login(request):
    return render(request, 'login.html')

def search(request):
    return render(request, 'search.html')

# สมัครสมาชิก
def billDetail(request, id):
    package = Package.objects.get(id=id)
    return render(request, 'billDetail.html', {'package':package})

def deliveryDetail(request, id):
    package = Package.objects.get(id=id)
    dataDictionary = {
        'name_package':'name_package',
        'price_package':'price_package',
    }
    dataJson = dumps(dataDictionary)
    return render(request, 'deliveryDetail.html', {'package':package, 'data':dataJson})

def searchdata(request):
    search_post = request.GET.get('q')
    if search_post:
        post = Register.objects.filter(Q(phone__icontains=search_post))
    else:
        return redirect("/")
    return render(request, 'searchdata.html', {'post':post})

# หน้าฟอร์มแจ้งการโอน
def payment(request, id):
    member = Register.objects.get(id=id) 
    return render(request, 'payment.html', {'member':member})

def bank(request):
    return render(request, 'bank.html')

# เพิ่มที่อยู่
def address(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        phone = request.POST.get('phone', False)
        address = request.POST.get('address', False)
        zone = request.POST.get('zone', False)
        district = request.POST.get('district', False)
        province = request.POST.get('province', False)
        ZIP_code = request.POST.get('ZIP_code', False)
        package = request.POST.get('package', False)
        choose_delivery = request.POST.get('choose_delivery', False)
        total_delivery = request.POST.get('total_delivery')
        
        if name == "" and phone == "" and address == "" and zone == "" and district == "" and province == "" and ZIP_code == "" and choose_delivery == ""and total_delivery == "":
            messages.info(request,"กรุณากรอกข้อมูลให้ครบถ้วน")
        else:
            add = Register.objects.create(
                name = name,
                phone = phone,
                address = address,
                zone = zone,
                district = district,
                province =province,
                ZIP_code = ZIP_code,
                package = package,
                choose_delivery = choose_delivery,
                total_delivery = total_delivery,
            )
            add.save()
            return redirect('bank')

#ฟังก์ชั่นลงทะเบียนลงฐานข้อมูล
def insertdata(request):
    if request.method == 'POST' and request.FILES['id_card'] and request.FILES['bankaccount'] and request.FILES['slip']:
        image_id_card = request.FILES['id_card']
        image_bank_account = request.FILES['bankaccount']
        image_slip = request.FILES['slip']
        gender = request.POST['gender']
        name = request.POST['name']
        phone = request.POST['phone']
        useremail = request.POST['useremail']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        bank = request.POST['bank']
        branch = request.POST['branch']
        recommender = request.POST['recommender']
        recommen = request.POST['recommen']
        package = request.POST['package']

        fs = FileSystemStorage()
        img_url1 = "id_card/"+image_id_card.name
        filename = fs.save(img_url1, image_id_card)
        img_url2 = "bankaccount/"+image_bank_account.name
        filename = fs.save(img_url2, image_bank_account)
        img_url3 = "slip/"+image_slip.name
        filename = fs.save(img_url3, image_slip)

        user = Member.objects.create(
            gender = gender,
            name = name,
            phone = phone,
            useremail = useremail,
            accountname = accountname,
            accountnumber = accountnumber,
            bank = bank,
            branch = branch,
            recommender =recommender,
            recommen = recommen,
            image_id_card = img_url1,
            image_bank_account = img_url2,
            image_slip = img_url3,
            package = package,
        )
        user.save()
        return redirect('home')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home_richest')
        else:
            messages.info(request,"รหัสสมาชิกและรหัสไม่ถูกต้อง")
            return redirect("login")

def admin(request):
    return render(request, 'admin')