from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view()),
    path('products/<int:id>',views.single_product),
    path('single_page_cart',views.single_page_cart),
    path('cart',views.Cart.as_view()),
    path('login',views.login),
    path('admindashboard',views.admin_index),
    path('myaccount',views.myaccount),
    path('account_information',views.account_information),
    path('address-book',views.address_book),
    path('ship_address',views.ship_address),
    path('add_new_address',views.add_new_address),
    path('checkout',views.Checkout.as_view(),name="checkout"),
    path('order',views.order),
    path('myorder',views.myorder),
    path('confirmation',views.confirmation),
    path('add_category',views.add_category),
    path('show_category',views.show_category),
    path('add_products',views.add_products),
    path('show_products',views.show_products),
    path('feature/<int:id>',views.feature_product),
    path('delete/<int:id>',views.delete_product),
    path('order_detail',views.order_detail),
    path('tracker_order',views.track_order),
    path('track_order_detail/<int:order_id>',views.track_order_detail),
    # path('Slider',views.Slider),
    # path('add_slider',views.add_slider),
    # path('show_slider',views.show_slider),
    # path('delete_slider/<int:id>',views.delete_slider),
    path('auth_login',views.auth_login),
    path('auth_register',views.auth_register),
    path('logout',views.logout)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)