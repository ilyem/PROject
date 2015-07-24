from django.shortcuts import render
from django.http import HttpResponse
from .models import Card


def index(request):
	card_image= Card.image
	return render(request, )
