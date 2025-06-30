from .models import Cart

def cart_context(request):
    if not request.user.is_authenticated:
        return {"cart_items": [], "cart_total_sum": 0}
    else:
        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        cart_total_sum = 0
        for cart_item in cart_items:
            cart_item.total_price = cart_item.quantity * cart_item.product.price
            cart_total_sum += cart_item.total_price
        return {"cart_items": cart_items, "cart_total_sum": cart_total_sum}
