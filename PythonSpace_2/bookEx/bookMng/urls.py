from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('search', views.search, name='search'),
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('mywishlist', views.mywishlist, name='mywishlist'),
    path('wishlist_delete/<int:wishlist_id>', views.wishlist_delete, name='wishlist_delete'),
    path('add_to_cart/<int:book_id>', views.add_to_cart, name='add_to_cart'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('cart_delete/<int:book_id>', views.cart_delete, name='cart_delete'),
    path('shopping_cartCheckout', views.shopping_cartSum, name = 'shopping_cartCheckout'),
    path('chatroom', views.chat, name='chatroom'),
    path('about_us', views.about_us, name='about_us'),
]