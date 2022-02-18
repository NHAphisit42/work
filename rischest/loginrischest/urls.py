from django.urls import path
from loginrischest import views

urlpatterns = [
    path('', views.home_richest, name='home_richest'),
    path('category/<slug:slug>', views.category_detail, name="product_by_category"),
    path('product', views.home_product, name='product'),
    path('product/<slug:slug>', views.detail, name='productDetail'),
    path('logout_backend', views.logout_backend, name='logout_backend'),
    path('proflie', views.home_proflie, name='home_proflie'),
    path('connect', views.home_connect, name='home_connect'),
    path('Order_History', views.Order_History, name='Order_History'),
    path('home_sale', views.home_sale,name='home_sale'),
    path('home_recommend', views.home_recommend, name='home_recommend'),
    path('home_point', views.home_point, name='home_point'),
    path('home_bonus', views.home_bonus, name='home_bonus'),
    path('detail_order', views.detail_order, name='detail_order'),
    path('cartdetail', views.cartdetail, name='cartdetail'),
    path('cart/add/<int:product_id>',views.addCart,name="addCart"),
    path('cart/remove/<int:product_id>',views.removeCart,name="removeCart"),
    path('updateuser', views.update_profile, name='update_profile'),
    path('searchProduct', views.searchproduct, name='searchproduct'),
    path('detail_announce/<int:id>', views.detail_announce, name='detail_announce'),
    path('updatecart/<int:id>', views.updatecart, name='updatecart'),
    path('order', views.order, name='order'),
]
