from django.shortcuts import render
from django.http import HttpResponse
from .models import Store

def store_index(request):
	title_page = "newsite - store page"
	prd = Store.objects.all()
	return render(request, 'store/product.html', {'title_page':title_page, 'prd':prd})

def prod_detail(request, pk):
	Store.objects.get(pk=pk)
	doc = Store.objects.filter(pk=pk)
	return render(request, 'store/product_document.html', {'pk':pk, 'doc':doc})
