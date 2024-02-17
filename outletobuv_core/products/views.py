from django.urls import reverse_lazy
from .forms import ProductImageForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Size, Material, Color, Category
from django.core.paginator import Paginator
from .utils import test, hide_product
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


class IndexView(TemplateView):
    template_name = 'products/index.html'
    title = 'Outlet Obuv'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 15
    title = 'Outlet obuv - Каталог'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('pk')
        return queryset.filter(category_id=category_id) if category_id else queryset
    
    def get_context_data(self, *, object_list=None, **krwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('category_id')
        product_color = self.object.color
        product_material = self.object.material
        product_size = self.object.size
        # sizes_query = Size.objects.filter(
        #                                   material=product_material,
        #                                   color=product_color
        #                                   )
        # try:
        #     unique_sizes = {size.value for size in sizes_query}
        #     sorted_unique_sizes = sorted(unique_sizes, key=int)
        # except:
        #     sorted_unique_sizes = sizes_query

        context['material'] = product_material
        context['color'] = product_color
        context['sizes'] = product_size

        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductImageForm
    template_name = 'product/update_product.html'
    success_url = reverse_lazy('update_product_image')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.image = self.request.FILES['image']
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:detail', kwargs={'pk': self.object.pk})
    

def search_by_name(request):
    query_data = request.GET.get('search_holder')
    query_article = Product.objects.filter(article__icontains=query_data)
    query_name = Product.objects.filter(name__icontains=query_data)
    query_size = Product.objects.filter(size__value__icontains=query_data)
    queryset = query_article | query_name | query_size
    categories = Category.objects.all()

    context = {
        'products': queryset,
        'categories': categories
    }
    
    return render(request, 'products/search.html', context)

def about(request):
    return render(request, 'products/about.html')

def parse_tsgoods_view(request):

    file_path = 'C:/Users/2021/Desktop/udemy/outletobuv_core/TSGoods.trs'

    try:
        test(file_path)
        return HttpResponse("File parsed successfully.")
    except Exception as e:
        print(e)
        return HttpResponse(f"Error occurred: {e}")
    
def hide(request):

    file_path = 'C:/Users/2021/Desktop/udemy/outletobuv_core/TSGoods.trs'

    try:
        hide_product(file_path)
        return HttpResponse("File parsed successfully.")
    except Exception as e:
        print(e)
        return HttpResponse(f"Error occurred: {e}")

def products2(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    
    per_page = 15
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    categories = Category.objects.all()
    context = {
        'title': 'Outlet Obuv',
        'categories': categories,
        'products': products_paginator,
    }
    return render(request, 'products/products2.html', context)
