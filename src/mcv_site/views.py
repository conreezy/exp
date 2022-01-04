from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
import requests
from requests import Request, Session
import json

from .forms import ContactForm
# from houses.models import HouseSale

def home_page(request):
    my_title = "Home"
    # qs = HouseSale.objects.all()[:6]
    context = {"title": my_title}#,'house_list': qs}
    return render(request, "index.html", context)

def home_search_page(request):
    my_title = "Home Search"

    ### --- DDF api
    url = 'https://data.crea.ca/Login.svc/Login'
    #parameters = {'id':'1',
     #             'convert':'CAD'}
    headers = {'username': '40re0H4jZqvcTSOaxBji22S0',
               'password': 'QB4zjCqcLSJgfZfKnDfjJe0m'} 

    session = Session()
    session.headers.update(headers)
    response = session.get(url)
    ddf_info = json.loads(response.text)

    template_name = "home_search.html"
    context = {"title": my_title, "ddf_info" : ddf_info}
    return render(request, "home_search.html", context)

def buyer_seminar_page(request):
    my_title = "FIRST TIME HOME BUYER SEMINAR OTTAWA"
    context = {"title": my_title}
    return render(request, "buyer_seminar.html", context)

def buyer_guide_page(request):
    my_title = "HOME BUYER GUIDE"
    context = {"title": my_title}
    return render(request, "buyer_guide.html", context)

def mortgage_calc_page(request):
    my_title = "MORTGAGE CALCULATOR"
    context = {"title": my_title}
    return render(request, "mortgage-calc.html", context)

def cash_flow_page(request):
    my_title = "BUYER GUIDE"
    context = {"title": my_title}
    return render(request, "cashflow-calc.html", context)

def consultation_page(request):
    my_title = "LISTING CONSULTATION"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    return render(request, "consultation.html", context)

def move_list_page(request):
    my_title = "MOVING CHECKLIST"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    return render(request, "move-list.html", context)

def resources_page(request):
    my_title = "RESOURCES"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    return render(request, "resources.html", context)

def renters_page(request):
    my_title = "RENTERS"
    context = {"title": my_title}
    return render(request, "renters.html", context)

def neighbourhood_page(request):
    my_title = "ABOUT US"
    context = {"title": my_title}
    return render(request, "neighbourhoods.html", context)

def contact_page(request):
    my_title = "CONTACT US"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": my_title, 
        "form": form
    }
    template_name = "contact.html"
    return render(request, template_name, context)

def testimonials_page(request):
    my_title = "TESTIMONIALS"
    context = {"title": my_title}
    template_name = "testimonials.html"
    return render(request, template_name, context)