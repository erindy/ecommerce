from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        'qs': queryset
    }

    return render(request, "products/product_list.html", context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context