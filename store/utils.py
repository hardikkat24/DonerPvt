import json
from .models import *
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
import datetime
import pytz 
from django.core.mail import EmailMessage
from django.utils.html import strip_tags


SHIPPING_CHARGES = 100
OWNER_MAIL = "saahillalwani3@gmail.com"


def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			cartItems += cart[i]['quantity']

			product = Product.objects.get(id=i)
			total = (product.price * cart[i]['quantity'])

			order['get_cart_total'] += total
			order['get_cart_items'] += cart[i]['quantity']

			item = {
				'id':product.id,
				'product':{
					'id':product.id,
					'name':product.lot_no, 
					'price':product.price, 
				        'imageURL':product.imageURL
					}, 
				'quantity':cart[i]['quantity'],
				
				'get_total':total,
				}
			items.append(item)

			if product.digital == False:
				order['shipping'] = True
		except:
			pass
			
	return {'cartItems':cartItems ,'order':order, 'items':items}


def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}

	
def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Product.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=item['quantity'],
		)

	return customer, order


def sendMail(request, order):
	current_site = get_current_site(request)
	mail_subject = "Your order Summary"
	totalcarat = grandtotal = 0

	for orderitem in order.orderitem_set.all():
		totalcarat += orderitem.product.carat
		grandtotal += orderitem.product.price

	grandtotal += SHIPPING_CHARGES

	message = render_to_string('store/customer_email.html',{
			'user': request.user,
			'datetime': datetime.datetime.now(pytz.timezone('Asia/Kolkata')),
			'order': order,
			'totalcarat': totalcarat,
			'grandtotal': grandtotal,
			'shipping_charges': SHIPPING_CHARGES,
			'request': request,
		})


	to_email = request.user.email

	email = EmailMessage(
			mail_subject, message, to = [to_email, OWNER_MAIL]
		)
	# email.attach(plain_message, "text/html")
	email.content_subtype = "html"
	# email.attach_file('static/images/Transparent-small.png')
	email.send()
	print("Sent")

"""
For getting choices while productions

def clarityChoices():
	products = Product.objects.all()
	list = []

	for product in products:
		if (product.clarity, product.clarity) not in list:
			list.append((product.clarity, product.clarity))

	return list


def colorChoices():
	products = Product.objects.all()
	list = []

	for product in products:
		if (product.color, product.color) not in list:
			list.append((product.color, product.color))

	return list


def shapeChoices():
	products = Product.objects.all()
	list = []

	for product in products:
		if (product.shape, product.shape) not in list:
			list.append((product.shape, product.shape))

	return list
"""

