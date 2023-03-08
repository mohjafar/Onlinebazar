from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.shoppage),
    path('single/<int:id>/',views.singlepage),
    path('login/',views.loginpage),
    path('logout/',views.logoutpage),
    path('sinup/',views.sinuppage),
    path('profile/',views.profilepage),
    path('update/',views.updateprofile),
    path('add-to-cart/<int:id>/',views.addToCart),
    path('cart/',views.cartPage),
    path('delete-cart/<int:pid>/',views.deleteCart),
    path('update-cart/<int:pid>/<str:op>',views.updatecart),
    path('addtowishlist/<int:pid>/',views.wish),
    path('delete-Wishlist/<int:pid>/',views.deleteWishlist),
    path('checkout/',views.Check),
    path('order/',views.orderpage),
    path('confirmation/',views.confirmationpage),
    path('contect/',views.contectpage),
    path('search/',views.searchpage),
    path('forgetusername/',views.forgeteuse),
    path('forgetotp/',views.forgetotp),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',views.paymentSuccess),
    path('newpassword/',views.password)
    


    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)