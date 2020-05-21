from .models import Product
import django_filters
from django import forms
from .models import COLOR_CHOICES, CLARITY_CHOICES, LAB_CHOICES

SHAPE_CHOICES_URL = [
	('AS', 'images/asscher.svg'),
	('CU', 'images/cushion.svg'),
	('EC', 'images/emerald.svg'),
	('HS', 'images/heart.svg'),
	('MQ', 'images/marquise.svg'),
	('OV', 'images/oval.svg'),
	('PR', 'images/princess.svg'),
	('PS', 'images/pear.svg'),
	('RA', 'images/radiant.svg'),
	('RD', 'images/round.svg'),
	('OTHER', 'images/other.svg'),
]


class ProductFilter(django_filters.FilterSet):
	shape = django_filters.MultipleChoiceFilter(field_name = 'shape', choices = SHAPE_CHOICES_URL, widget=forms.CheckboxSelectMultiple())
	color = django_filters.MultipleChoiceFilter(field_name = 'color', choices = COLOR_CHOICES, widget=forms.CheckboxSelectMultiple())
	clarity = django_filters.MultipleChoiceFilter(field_name = 'clarity', choices = CLARITY_CHOICES, widget=forms.CheckboxSelectMultiple())
	lab = django_filters.MultipleChoiceFilter(field_name = 'lab', choices = LAB_CHOICES, widget=forms.CheckboxSelectMultiple())

	price_gt = django_filters.NumberFilter(field_name = 'price', lookup_expr = 'gt')
	price_lt = django_filters.NumberFilter(field_name = 'price', lookup_expr = 'lt')
	carat_gt = django_filters.NumberFilter(field_name = 'carat', lookup_expr = 'gt')
	carat_lt = django_filters.NumberFilter(field_name = 'carat', lookup_expr = 'lt')

	class Meta:
		model = Product
		fields = ['shape', 'color', 'clarity', 'carat', 'lab']