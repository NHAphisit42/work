from os import name
from django.urls import path
from backendrischest import views

urlpatterns = [
    path('', views.home_backend, name='home_backend'),
    path('table_backend', views.table_backend, name='table_backend'),
    path('register_backend', views.register_backend, name='register_backend'),
    path('login_backend', views.login_backend, name='login_backend'),
    path('adduser_backend', views.adduser_backend, name='adduser_backend'),
    path('backend_login', views.backend_login, name='backend_login'),
    path('member_backend', views.member_backend, name='member_backend'),
    path('addmember_backend', views.addmember_backend, name='addmember_backend'),
    path('logout', views.logout_BE, name='logout'),
    path('remove', views.remove_backend, name='remove'),
    path('chartdiagram', views.chartdiagram, name='chartdiagram'),
    path('addmember', views.addmember, name='addmember'),
    
    
    # หน้าสินค้าและหมวดหมู่
    path('addproduct', views.addproduct_backend, name='addproduct_backend'),
    path('add_product', views.addproduct, name='addproduct'),
    path('addpackage', views.insetpackage, name='addpackage'),
    path('add_category', views.addcategory_backend, name='addcategory_backend'),
    path('category', views.addcategory, name='category'),
    path('table_package', views.table_package, name='table_package'),
    path('Addpackage', views.package, name='package'),
     path('table_product', views.tableproduct_backend, name='tableproduct'),
     path('table_category', views.categorytable, name='tablecategory'),
    
    # ลิงค์หน้าเว็บไซต์
    path('order/<int:id>', views.orderdetail, name='orderdetail'),
    path('member/<int:id>', views.memberdetail, name='member'),
    path('delivery/<int:id>/', views.remove_backend, name='remove'),
    path('register/<int:id>', views.removeregister_backend, name='removeregister'),
    path('product/<int:id>', views.productdeatil, name='detail'),
    path('removepackage/<int:id>', views.removepackage, name='remove_package'),
    path('package/<int:id>', views.packagedetail, name='package_detail'),
    path('approve/<str:status_id>', views.approve, name='approve'),
    path('disapprove/<str:status_id>',views.disapprove, name='disapprove'),
    path('update/<int:id>', views.updateproduct, name='update'),
    path('updatepackage/<int:id>', views.updatepackage, name='updatepackage'),
    path('removeproduct/<int:id>', views.removeproduct, name='remove_product'),
]
