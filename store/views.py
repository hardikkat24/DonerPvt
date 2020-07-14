from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder, sendMail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm, ShippingAddressForm, CustomerSignUpForm, ProductUpdateForm, QuantityForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProductFilter
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import messages

def store(request):
	"""

	"""
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.filter( ordered__exact = False )
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


@login_required
def add(request, pk):
	product = Product.objects.get(pk = pk)
	order, created = Order.objects.get_or_create(customer = request.user.customer, complete = False)
	orderitem, orderitemcreated = OrderItem.objects.get_or_create(product = product, order = order)
	if not orderitemcreated:
		messages.info(request, '<p style="color: Red">Item already in cart!</p>')

	return redirect('search')

@login_required
def add2(request, pk):
    product = Product.objects.get(pk = pk)
    order, created = Order.objects.get_or_create(customer = request.user.customer, complete = False)
    orderitem, orderitemcreated = OrderItem.objects.get_or_create(product = product, order = order)
    if not orderitemcreated:
         messages.info(request, 'Item already in cart!')
    return redirect('store')

@login_required
def remove(request, pk):
	orderitem = OrderItem.objects.get(pk = pk)
	orderitem.delete()

	return redirect('cart')

@login_required
def update(request):

	add, _ = ShippingAddress.objects.get_or_create(customer = request.user.customer)
	print(add)

	if request.method == "POST":
		form = ShippingAddressForm(request.POST, instance = add)
		if form.is_valid():
			form.save()

	else:
		form = ShippingAddressForm(instance = add)

	context = {
		'form': form
	}

	return render(request, "store/update.html", context)


@login_required
def view(request, pk):
	product = Product.objects.filter(lot_no__exact = pk).first()
	if request.method == "POST":
		form = QuantityForm(request.POST)
		if form.is_valid():
			quantity = form.cleaned_data.get('quantity')
			order, created = Order.objects.get_or_create(customer = request.user.customer, complete = False)
			orderitem, orderitemcreated = OrderItem.objects.get_or_create(product = product, order = order)

			orderitem.quantity = quantity
			if orderitem.quantity > orderitem.product.stone:
				orderitem.quantity = orderitem.product.stone
				messages.info(request, 'Only '+ str(orderitem.product.stone) + "piece(s) left !" )

			orderitem.save()



	data = cartData(request)

	cartItems = data['cartItems']
	form = QuantityForm()

	context = {
	'product': product,
	'cartItems':cartItems,
	'form': form,
	}
	return render(request, "store/product.html", context)


@login_required
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)


@login_required
def place_order(request):
	order = Order.objects.get(customer = request.user.customer, complete = False)

	if order.orderitem_set.count() > 0:
		order.complete = True
		order.save()
		sendMail(request, order)

		for orderitem in order.orderitem_set.all():
			orderitem.product.stone -= orderitem.quantity
			if orderitem.product.stone <= 0:
				orderitem.product.ordered = True
			orderitem.product.save()
		return redirect('success')


@login_required
def search(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	product_list = Product.objects.filter(ordered__exact = False)
	product_filter = ProductFilter(request.GET, queryset = product_list)
	product_list = product_filter.qs

	# for p in product_list:
	# 	print(p)
	# page = request.GET.get("page", 1)
	# paginator = Paginator(product_list, 50)

	# try:
	# 	products_p = paginator.page(page)
	# except PageNotAnInteger:
	# 	products_p = paginator.page(1)
	# except EmptyPage:
	# 	products_p = paginator.page(paginator.num_pages)
	# print(products_p)
	context = {'products':product_list, 'cartItems':cartItems, 'filter': product_filter}
	return render(request, 'store/products.html',context)


def login_view(request):
    form = LoginForm(request.POST or None)
    protocol = "http://"
    if request.is_secure():
    	protocol = "https://"
    if request.GET.get('next') is not None:
    	redirect1 = protocol + request.META['HTTP_HOST'] + request.GET.get('next')

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next') is None:
            	return redirect('store')
            return HttpResponseRedirect(redirect1)
    return render(request, "store/login.html", {"form": form})


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        form1 = CustomerSignUpForm(request.POST)
        form2 = ShippingAddressForm(request.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save()

            customer = form1.save(commit = False)
            customer.user = user
            customer.save()

            address = form2.save(commit = False)
            address.customer = user.customer
            address.save()

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/login/")
    else:
        form = SignUpForm()
        form1 = CustomerSignUpForm()
        form2 = ShippingAddressForm()
    return render(request, "store/register.html", {"form": form, 'form1':form1, 'form2': form2})


def about(request):
	return render(request, 'store/about.html')

@login_required
def successfulOrder(request):
	return render(request, "store/success.html")


@login_required
def addImage(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	if request.user.is_superuser:

		product_list = Product.objects.filter( ordered__exact = False )


		context = {'products':product_list, 'cartItems':cartItems}
		return render(request, 'store/add_image.html',context)
	else:
		messages.info(request, "NOT ALLOWED!")
		return redirect('store')


@login_required
def addImageUpdate(request, pk):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	if request.user.is_superuser:
		product = Product.objects.filter( lot_no__exact = pk ).first()

		if request.method == "POST":
			print('post yes')
			form = ProductUpdateForm(request.POST or None, request.FILES, instance = product)
			if form.is_valid():
				form.save()
				return redirect('add_image')
			else:
				print("HERE")

		else:
			product = Product.objects.get( pk = pk )
			form = ProductUpdateForm(instance = product)

		context = {'form':form, 'cartItems':cartItems}
		return render(request, 'store/add_image_detail.html',context)

	else:
		messages.info(request, "NOT ALLOWED!")
		return redirect('store')


"""
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

	def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)



@login_required
def checkout(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	if request.method == "POST":
		form = ShippingAddressForm(request.POST)
		if form.is_valid():
			ins = form.save(commit = False)
			order1 = Order.objects.get(customer = request.user.customer, complete = False)

			if order1.orderitem_set.count() > 0:
				order1.complete = True
				order1.save()
				ins.order = order1
				ins.customer = request.user.customer
				ins.save()
				sendMail(request, order1)

				for orderitem in order.orderitem_set.all():
					orderitem.product.stone -= orderitem.quantity
					if orderitem.product.stone <= 0:
						orderitem.product.ordered = True
					orderitem.product.save()
				return redirect('success')
			else:
				messages.info(request, "No items in cart!")
			form = ShippingAddressForm()

	else:
		form = ShippingAddressForm()


	context = {'items':items, 'order':order, 'cartItems':cartItems, 'form': form}
	return render(request, 'store/checkout.html', context)


<!-<tr><td style="white-space:nowrap;font-family:'trebuchet ms','helvetica',sans-serif;font-size:13px" valign="top" align="left">&lt;&lt; doner diamonds png&gt;&gt;</td></tr>-!>
"""
