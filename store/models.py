from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


SHAPE_CHOICES = [
	('OTHER', 'OTHER'),
	('RD', 'Round'),#
	('AS', 'Asscher'),#
	('CU', 'Cushion'),#
	('EC', 'Emerald'),#
	('HS', 'Heart'),#
	('MQ', 'Marquise'),#
	('OV', 'Oval'),#
	('PR', 'Princess'),#
	('PS', 'Pear Shape'),#
	('RA', 'Radiant'),#
]

PSEUDO_SHAPE_CHOICES = [
    ('RD', 'Round'),#
	('BU', 'BU1'),
	('CU', 'Cushion'),#
	('EC', 'Emerald'),#
	('EU', 'EU1'),
	('HS', 'Heart'),#
	('MQ', 'Marquise'),#
	('OV', 'Oval'),#
	('OM', 'OM1'),
	('PR', 'Princess'),#
	('PS', 'Pear Shape'),#
	('RA', 'Radiant'),#
	('RD', 'Round'),#
	('AS', 'Asscher'),#
	('STB', 'STB1'),
	('TB', 'TB1'),
	('TR', 'TR1'),
]

x = [p[0] for p in SHAPE_CHOICES]

CLARITY_CHOICES = [
	('FL', 'FL'),
	('IF', 'IF'),
	('VVS1', 'VVS1'),
	('VVS2', 'VVS2'),
	('VS1', 'VS1'),
	('VS2', 'VS2'),
	('SI1', 'SI1'),
	('SI2', 'SI2'),
	('SI3', 'SI3'),
	('I1', 'I1'),
	('I2', 'I2'),
]

COLOR_CHOICES = [
	('D', 'D'),
	('E', 'E'),
	('F', 'F'),
	('G', 'G'),
	('H', 'H'),
	('I', 'I'),
	('J', 'J'),
	('K', 'K'),
	('L', 'L'),
	('M', 'M'),
	('N', 'N'),
]
FLOUROSCENE_CHOICES = [
    ('N', 'NONE'),
	('F', 'FAINT'),
	('M', 'MEDIUM'),
	('S', 'STRONG'),
	('VS','VERY STRONG')
]


LAB_CHOICES = [
	('GIA', 'GIA'),
	('EGL USA', 'EGL USA'),
	('OWN', 'Non-Certified')
]

CUT_CHOICES = [
	('EX', 'EX'),
	('VG', 'VG'),
	('G','GD'),
	('F', 'FR'),
]
SYM_CHOICES = [
	('X', 'EX'),
	('VG', 'VG'),
	('G','GD'),
	('F', 'FR'),
]
POL_CHOICES = [
	('EX', 'EX'),
	('VG', 'VG'),
	('G','GD'),
	('F', 'FR'),
]

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=False, blank = False)
	company_name = models.CharField(max_length=200, null=False, blank = False)

	def __str__(self):
		return self.user.username

"""
def create_customer(sender, instance, created, **kwargs):
	if created:
		profile, created = Customer.objects.get_or_create(user = instance)

post_save.connect(create_customer, sender = User)
"""

class Product(models.Model):

	name = models.CharField(max_length=200, null = True, blank = True, default = "-")
	lot_no = models.CharField(primary_key = True, max_length = 30)
	shape = models.CharField(max_length = 20, choices = SHAPE_CHOICES)
	pseudo_shape = models.CharField(max_length = 20, choices = PSEUDO_SHAPE_CHOICES, default = "OTHER")
	carat = models.FloatField(null = True, blank = True)
	stone = models.IntegerField(null = True, blank = True) # Quantity
	color = models.CharField(max_length = 25, choices = COLOR_CHOICES, default = "D")
	clarity = models.CharField(max_length = 25, choices = CLARITY_CHOICES, default = "FL")
	measurement = models.CharField(max_length = 50, null = True, blank = True)
	dept = models.FloatField(null = True, blank = True)
	tbl = models.IntegerField(null = True, blank = True)
	cut = models.CharField(max_length = 100,choices=CUT_CHOICES, null = True, blank = True, default = "-")
	pol = models.CharField(max_length = 10,choices=POL_CHOICES, null = True, blank = True, default = "-")
	sym = models.CharField(max_length = 10,choices=SYM_CHOICES, null = True, blank = True, default = "-")
	fl = models.CharField(max_length = 10,choices=FLOUROSCENE_CHOICES, null = True, blank = True, default = "-")
	cul = models.CharField(max_length = 10, null = True, blank = True, default = "-")
	girdle = models.CharField(max_length = 50, null = True, blank = True, default = "-")
	lab = models.CharField(max_length = 25, choices = LAB_CHOICES, default = "OWN")
	certno = models.CharField(max_length = 40, null = True, blank = True, default = "-")
	rap = models.FloatField(null = True, blank = True)
	price = models.FloatField(null = True, blank = True)
	image = models.URLField(null = True, blank = True)
	certificate = models.URLField(null = True, blank = True)
	ordered = models.BooleanField(default = False)
	video = models.URLField(null = True, blank = True, default = '')




	def __str__(self):
		return str(self.lot_no)

	@property
	def price_ct(self):
		return self.price / self.carat


	@property
	def imageURL(self):
		try:
			url = self.image
		except:
			url = ''
		return url

	@property
	def certificateURL(self):
		try:
			url = self.certificate
		except:
			url = ''
		return url

	def save(self, *args, **kwargs):
		self.pseudo_shape = self.shape
		if self.shape not in x:
			self.shape = "OTHER"
		if self.stone > 0:
			self.ordered = False
		super(Product, self).save(*args, **kwargs)


	class Meta:
   		ordering = ['lot_no']



class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	"""
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping
	"""

	@property
	def shipping(self):
		return True

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=1, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	country = models.CharField(max_length=200, null=False, default = "India", blank = False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address