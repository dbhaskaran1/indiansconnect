# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def view_site(request):
    return render (request, 'connect/index.html', {} )

def aboutus(request):
    return render (request, 'connect/carousel.html')
