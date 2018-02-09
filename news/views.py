from django.shortcuts import render
from django.http import HttpResponse

def news(request):
	return HttpResponse("it's a news for bboy's")