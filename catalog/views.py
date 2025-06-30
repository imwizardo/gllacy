from django.shortcuts import render
from .models import Product
from forms.forms import FilterForm

def catalog(request):
    products = Product.objects.all()
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            fat = form.cleaned_data.get("fat", None)
            selected_fillers = form.cleaned_data.get("fillers", None)
            min_price = form.cleaned_data.get("min_price", None)
            max_price = form.cleaned_data.get("max_price", None)
            if fat:
                # if fat == "fat=0":
                #     products = products.filter(fat=0)
                # elif fat == "fat__lte=10":
                #     products = products.filter(fat__lte=10)
                # elif fat == "fat__lte=30":
                #     products = products.filter(fat__lte=30)
                # elif fat == "fat__gt=30":
                #     products = products.filter(fat__gt=30)
                # global_dict = {}
                # exec(f"products = products.filter({fat})", globals(), global_dict)
                # products = global_dict["products"]
                filters = {
                    '0': {'fat': 0},
                    'up to 10': {'fat__lte': 10},
                    'up to 30': {'fat__lt': 30},
                    'above to 30': {'fat__gte': 30},
                }
                filter_params = filters.get(fat)
                if filter_params:
                    products = products.filter(**filter_params)
            if selected_fillers:
                products = products.filter(fillers__name__in=selected_fillers).distinct()
            if min_price:
                products = products.filter(price__gte=min_price)
            if max_price:
                products = products.filter(price__lte=max_price)
    return render(request, "catalog.html", context={"products": products})

