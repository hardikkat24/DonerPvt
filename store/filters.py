from .models import Product
import django_filters
from django import forms
from .models import COLOR_CHOICES, CLARITY_CHOICES, LAB_CHOICES, FLOUROSCENE_CHOICES,CUT_CHOICES,SYM_CHOICES,POL_CHOICES

SHAPE_CHOICES_URL = [
	('RD', 'images/round.svg'),
	('PR', 'images/princess.svg'),
	('OV', 'images/oval.svg'),
	('MQ', 'images/marquise.svg'),
	('EC', 'images/emerald.svg'),
	('AS', 'images/asscher.svg'),
	('PS', 'images/pear.svg'),
	('HS', 'images/heart.svg'),
	('CU', 'images/cushion.svg'),
	('RA', 'images/radiant.svg'),
	('OTHER', 'images/other.svg'),
]



class ProductFilter(django_filters.FilterSet):
	shape = django_filters.MultipleChoiceFilter(field_name = 'shape', choices = SHAPE_CHOICES_URL, widget=forms.CheckboxSelectMultiple())
	color = django_filters.MultipleChoiceFilter(field_name = 'color', choices = COLOR_CHOICES, widget=forms.CheckboxSelectMultiple())
	clarity = django_filters.MultipleChoiceFilter(field_name = 'clarity', choices = CLARITY_CHOICES, widget=forms.CheckboxSelectMultiple())
	lab = django_filters.MultipleChoiceFilter(field_name = 'lab', choices = LAB_CHOICES, widget=forms.CheckboxSelectMultiple())
	fl = django_filters.MultipleChoiceFilter(field_name = 'fl', choices = FLOUROSCENE_CHOICES, widget=forms.CheckboxSelectMultiple())
	cut = django_filters.MultipleChoiceFilter(field_name = 'cut', choices = CUT_CHOICES, widget=forms.CheckboxSelectMultiple())
	sym = django_filters.MultipleChoiceFilter(field_name = 'sym', choices = SYM_CHOICES, widget=forms.CheckboxSelectMultiple())
	pol = django_filters.MultipleChoiceFilter(field_name = 'pol', choices = POL_CHOICES, widget=forms.CheckboxSelectMultiple())

	price_gt = django_filters.NumberFilter(field_name = 'price', lookup_expr = 'gt')
	price_lt = django_filters.NumberFilter(field_name = 'price', lookup_expr = 'lt')
	carat_gt = django_filters.NumberFilter(field_name = 'carat', lookup_expr = 'gt')
	carat_lt = django_filters.NumberFilter(field_name = 'carat', lookup_expr = 'lt')
	diss_gt = django_filters.NumberFilter(field_name = 'rap', lookup_expr = 'gt')
	diss_lt = django_filters.NumberFilter(field_name = 'rap', lookup_expr = 'lt')

	class Meta:
		model = Product
		fields = ['shape', 'color', 'clarity', 'carat', 'lab','fl','cut','sym','pol']