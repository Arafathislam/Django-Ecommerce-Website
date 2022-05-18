from dango.urls import path
from .import views


urlpatterns=[
    path(' ',views.sotre,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    
]