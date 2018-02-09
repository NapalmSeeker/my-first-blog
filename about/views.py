from django.shortcuts import render
from django.http import HttpResponse

def about(request):
	return HttpResponse("it's a about for bboy's")