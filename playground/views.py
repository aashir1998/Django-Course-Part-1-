from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
    try:
        # select related is used when we have only one related item, like in this case we have collection
        # prefetch _related is used when we have multiple related items like promotions
        queryset = (
            Product.objects.prefetch_related("promotions")
            .select_related("collection")
            .all()
        )

    except ObjectDoesNotExist:
        pass
    return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
