from django.shortcuts import render, redirect
from .forms import EmailForm, FeedbackForm, SearchForm
from .models import Email, Feedback
from catalog.models import Product

def email_form(request):
    form = EmailForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data["email"]
        e = Email()
        e.email = email
        e.save()
    return redirect("home_url")

def feedback_form(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        text = form.cleaned_data["text"]
        e = Feedback()
        e.name = name
        e.email = email
        e.text = text
        e.save()
    else:
        print(form.errors)
    return redirect("home_url")

def search_form(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            search_value = form.cleaned_data["search_value"]
            products = Product.objects.filter(name__icontains=search_value)
            return render(request, "catalog.html", context={"products": products})