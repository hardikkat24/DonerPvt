from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class ProductResource(resources.ModelResource):

	class Meta:
		model = Product
		exclude = ('name', 'ordered', 'pseudo_shape', 'image')
		import_id_fields = ['lot_no',]


class ProductAdmin(ImportExportModelAdmin):
	resource_class = ProductResource


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Jewellery)