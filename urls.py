from django.urls import path
from myapp import views
from myapp import cart
from myapp import cartremove
from myapp import checkout
from myapp import collections
from myapp import collectionsview
from myapp import addcart
from myapp import fav
from myapp import favremove
from myapp import favview
from myapp import login
from myapp import placeorder
from myapp import productdetail
from myapp import register
from myapp import signout




urlpatterns= [
    path('',views.home,name="home"),
    path('register',register.register,name="register"),
    path('login',login.login_page,name="login"),
    path('collections',collections.collections,name="collections"),
    path('collections/<str:name>',collectionsview.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',productdetail.product_details,name="product_details"),
    path('addtocart',addcart.add_to_cart,name="addtocart"),
    path('cart',cart.cart_page,name="cart"),
    path('remove_cart/<str:cid>',cartremove.remove_cart,name="remove_cart"),
    path('fav',fav.fav_page,name="fav"),
    path('remove_fav/<str:fid>',favremove.remove_fav,name="remove_fav"),
    path('favviewpage',favview.favviewpage,name="favviewpage"),
    path('signout',signout.signout,name='signout'),
    path('checkout',checkout.checkout,name='checkout'),
    path('placeorder',placeorder.placeorder,name='placeorder'),
    path('proceed-to-pay',views.razorpaycheck)

   
    

]