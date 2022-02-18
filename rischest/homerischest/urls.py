from django.urls import path
from homerischest import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('search', views.search, name='search'),
    path('payment/<str:id>', views.payment, name='payment'),
    path('register/billDetail/<str:id>', views.billDetail, name='billDetail'),
    path('register/deliveryDetail/<str:id>', views.deliveryDetail, name='deliveryDetail'),
    path('insertdata', views.insertdata, name='insertdata'),
    path('bank', views.bank, name='bank'),
    path('searchdata', views.searchdata, name='searchdata'),
    path('login_views', views.login_view, name='login_views'),
    path('admin/', views.admin, name='admin'),
    path('address', views.address, name='address'),
]
