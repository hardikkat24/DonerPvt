from django.urls import path
from django.conf import settings
from . import views
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('add/<str:pk>', views.add, name = "add"),
        path('add2/<str:pk>', views.add2, name = "add2"),
	path('remove/<str:pk>', views.remove, name = "remove"),
	path('view/<str:pk>', views.view, name = "view"),
	path('cart/', views.cart, name="cart"),
	# path('checkout/', views.checkout, name="checkout"),
	path('place-order/', views.place_order, name="place-order"),
	path('enquiry/', views.enquiry, name="enquiry"),
	path('search/', views.search, name="search"),
	path('login/', login_view, name="login"),
   	path('register/', register_user, name="register"),
  	path("logout/", LogoutView.as_view(), name="logout"),
  	path('update/', views.update, name="update"),
	# path('update_item/', views.updateItem, name="update_item"),
	# path('process_order/', views.processOrder, name="process_order"),
	path('about_us/', views.about, name="about"),
	path('success/', views.successfulOrder, name="success"),
	path('addImage/', views.addImage, name='add_image'),
	path('addImageUpdate/<str:pk>', views.addImageUpdate, name='add_image_update'),
	path('jewellery/', views.jewellery, name = "jewellery"),

	path('ajax/enquiry/', views.ajax_enquiry, name = "ajax-enquiry"),
	path('ajax/cart/', views.ajax_cart, name = "ajax-cart"),
]
