from django.shortcuts import render
from django.http import HttpResponse

def home_index(request):
	title_page = "newsite - home page"
	return render(request, 'home/base_page.html', {'title_page':title_page})