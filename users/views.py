from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from .models import Cart, CartItem
from catalog.models import Product

def register_form(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home_url")
        else:
            print(form.errors)
    form = UserRegistrationForm()
    return render(request, "register.html", context={"form": form})

@login_required
def personal_account(request):
    user = request.user
    profile_form = UserProfileForm(instance=user)
    password_form = PasswordChangeForm(user)
    if request.method == "POST":
        if "profile_submit" in request.POST:
            profile_form = UserProfileForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Ваш профиль успешно обновлён")
                return redirect("personal_account_url")
            else:
                messages.error(request, "Пожалуйста исправьте ошибки ниже")
        elif "password_submit" in request.POST:
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Ваш пароль успешно обновлён")
                return redirect("personal_account_url")
            else:
                messages.error(request, "Пожалуйста исправьте ошибки ниже")

    return render(request, "personal_account.html", context={"profile_form": profile_form, "password_form": password_form})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not cart_item_created:
        cart_item.quantity+=1
        cart_item.save()
    referrer = request.META.get("HTTP_REFERER")
    return redirect(referrer)

def delete_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user)
    cart_item = cart.items.filter(product=product).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    referrer = request.META.get("HTTP_REFERER")
    return redirect(referrer)